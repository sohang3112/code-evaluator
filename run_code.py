from argparse import ArgumentParser, FileType
from tempfile import gettempdir
from pathlib import Path
from itertools import chain
import datetime

# User Defined
from language import Language
from utils import load_yaml, validate_requirements

# defaults
DEFAULT_CONFIG = Path('default_config.yaml')
DEFAULT_TEMP_DIR = Path(gettempdir())

if __name__ == '__main__':
    parser = ArgumentParser(description='Tests Student Code Submissions')
    parser.add_argument(
        'tests', type=Path, help='YAML file which contains a list of tests')
    parser.add_argument(
        '--config', nargs='?', type=FileType, default=DEFAULT_CONFIG,
        help='Path to YAML Configuration file')
    parser.add_argument(
        '--timeout', nargs='?', type=int, default=None,
        help='Max Time (in seconds) allowed for a code submission to give the result of 1 test. '
             'None (default) means no timeout.')
    parser.add_argument(
        '--temp', nargs='?', type=Path, default=DEFAULT_TEMP_DIR,
        help='Directory for storing temporary files')

    args = parser.parse_args()
    config = load_yaml(args.config)
    timeout = args.timeout and datetime.time(second=args.timeout)
    temp_dir = args.temp

    languages = [Language(name=lang, **params) for lang, params in config.languages.items()]
    validate_requirements(chain.from_iterable(lang.requirements for lang in languages))

    # TODO - check that all file paths are correct (config, temp, tests)
    # TODO - extract list of tests from tests file
