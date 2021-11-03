from pathlib import Path
from typing import Dict, List, NamedTuple
import re

# NAMING CONVENTIONS
# pattern -> regex string,      regex -> re.compile(pattern) [COMPILED REGEX]

# Windows specific
# TODO - load commands inside sandbox
commands = {
    'c': 'g++ -std=c99 {name}.c -o {name}.exe'              # C
    'cpp': 'g++ -std=c++17 {name}.cpp -o <name>.exe'        # C++
    'python': 'python3 {name}.py'                           # Python 3
}

# Defaults
test_dir_defaults = {
    'code': '../code',
    'input': '../test-input',
    'output': '../test-output',
    'rte': '../test-output',        # runtime error - by default, same dir as output
    'cte': '../test-output'         # compile time error - by default, same dir as output
}

test_file_formats = {
    'code':   '{course}.{student}.{extension}',
    'input':  'test{num}.input',                
    'output': '{student}.{num}.output',
    'rte':    '{student}.{num}.rte',
    'cte':    '{student}.{num}.cte'
}


# TODO - Test This - Complicated Function (parse_params)

# Inspired by: https://stackoverflow.com/a/15175239/12947681
# However, unlike that answer, here I'm NOT escaping param names (keys),
# because they are internal only, so there is no danger of messing up regex
def _make_regex_pattern_from_format_string(format_str: str,
                                   *param_names: List[str]) -> str:
    pattern = '{(%s)}' % '|'.join(param_names)

    # ans_pattern contains named capture groups ?P<...>, that are used later while
    # matching
    ans_pattern = re.sub(pattern, '(?P<\1>:.*?)')   # this should be global replace - check!!
    return ans_pattern

# Note: DON'T GET param_names from user input - or if you do, sanitize it first
# Any parameter name in param_names must NOT contain any special character
# that is used in regex
def parse_params(filename: str,
                 format_str: str,
                 *param_names: List[str]) -> Dict[str, str]:
    pattern = _make_regex_pattern_from_format_string(format_str, *param_names)
    match = re.match(pattern, filename)
    if match is None:
        raise ValueError(
            f'File Name {filename} could not be parsed using format string {format_str}, '
            f'parameters {param_names}'
        )
    return { param : match.group(param) for param in param_names }




    
    
        

