from typing import Any, Iterable, List
from types import SimpleNamespace
from pathlib import Path
import subprocess
import yaml

# User Defined
from command import Command


def load_yaml(yaml_path: Path) -> SimpleNamespace:
    """Loads YAML from input path"""
    with yaml_path.open() as stream:
        return SimpleNamespace(**yaml.safe_load(stream))


def shell_command_not_exists(command: Command) -> bool:
    status, result = subprocess.getstatusoutput(command + ' --version')
    return status != 0


def validate_requirements(commands: Iterable[Command]) -> None:
    """Throws error if any command is not present in shell"""
    unsatisfied = list(filter(shell_command_not_exists, commands))
    if unsatisfied:
        raise OSError('Shell Commands not found: ' + ', '.join(unsatisfied))


def lines(output: str) -> List[str]:
    """Discard whitespace at start and end of each line, as well as any blank lines at the end of output"""
    return [line.strip() for line in output.rstrip('\n').split('\n')]
