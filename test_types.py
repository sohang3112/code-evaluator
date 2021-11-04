from __future__ import annotations

from typing import List, NamedTuple, Optional
from enum import Enum
import subprocess
import datetime

# User Defined
from utils import lines
from command import Command


# type aliases
CompileTimeError = str
TestInput = str


class TestOutput(NamedTuple):
    lines: List[str]

    @staticmethod
    def parse(output: str) -> TestOutput:
        return TestOutput(lines(output))


class TestStatus(Enum):
    passed = 1
    failed = 2
    runtime_error = 3
    timeout_error = 4


# Note: if status == TestStatus.time_out, then value of output is irrelevant
class TestResult(NamedTuple):
    status: TestStatus
    output: str


class Test:
    def __init__(self, input: TestInput, output: TestOutput):
        self.input = input
        self.output = output

    def compare_with_actual(self, returncode: int, output: str) -> TestStatus:
        if returncode != 0:
            return TestStatus.runtime_error
        elif TestOutput.parse(output) != self.output:
            return TestStatus.failed
        else:
            return TestStatus.passed

    # TODO - return status TestStatus.timeout_error when code takes too long (using timeout parameter)
    def run(self, command: Command, timeout: Optional[datetime.time] = None) -> TestResult:
        try:
            proc = subprocess.run(command, capture_output=True, input=self.input, encoding='ascii',
                                  timeout=timeout and timeout.second)
            return TestResult(status=self.compare_with_actual(proc.returncode, proc.stdout),
                              output=proc.stdout)
        except subprocess.TimeoutExpired:
            return TestResult(TestStatus.timeout_error, '')