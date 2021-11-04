from typing import NamedTuple, Iterable, List, Optional, Union
from subprocess import getstatusoutput
import datetime

# User Defined
from test_types import Test, TestResult, CompileTimeError
from command import Command


class Language(NamedTuple):
    name: str
    requirements: List[Command]
    compile: Command
    execute: Command

    def run(self, tests: Iterable[Test],
                  timeout: Optional[datetime.time] = None,
                  **kwargs) -> Union[CompileTimeError, List[TestResult]]:
        # TODO - Should I use timeout during compilation also??
        compiler_status, compiler_output = getstatusoutput(self.compile.format(**kwargs))
        if compiler_status != 0:
            return CompileTimeError(compiler_output)

        run_command = self.execute.format(**kwargs)
        return [test.run(run_command, timeout) for test in tests]
