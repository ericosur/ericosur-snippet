'''
Module store provides useful utilities

how to export functions
1. import functions from xxxx_util
2. add name of functions into the list: __all__
'''


# __init__.py

__VERSION__ = '2024.11.26'

from .commonutil import clamp
from .commonutil import get_home, print_stderr, read_from_stdin
from .commonutil import is_path_exist, isfile, isdir, mkdir
from .debug_verbose import MyDebug, MyVerbose, die, prt
from .hashutil import md5sum, sha1sum, sha256sum, sha384sum, sha512sum, sha3_256sum, sha3_512sum
from .jsonutil import read_setting, read_textfile, read_jsonfile, write_jsonfile
from .mydateutil import get_dow, is_leapyear, get_offset_from_year, get_doom_num
from .pathutil import DefaultConfig
from .queryutil import query_url_for_data, query_url_for_json
from .run_cmd import run_command, run_command2, show_platform
from .thedatetime import get_epoch, WhatNow
from .versionutil import get_python_version, get_python_versions, require_python_version
from .__myutil import is_linux, is_cygwin, is_windows, get_platform

def sep():
    ''' sep '''
    print('-------------------------')

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

is_file = isfile
is_dir = isdir

# sort by alphatic if possible
__all__ = [
    'clamp',
    'die',
    'do_nothing',
    'get_dow',
    'get_doom_num',
    'get_epoch',
    'get_home',
    'get_offset_from_year',
    'get_platform',
    'get_python_version',
    'get_python_versions',
    'is_cygwin',
    'is_dir',
    'is_file',
    'is_leapyear',
    'is_linux',
    'is_path_exist',
    'is_windows',
    'isdir',
    'isfile',
    'md5sum',
    'mkdir',
    'print_stderr',
    'prt',
    'query_url_for_data',
    'query_url_for_json',
    'read_from_stdin',
    'read_jsonfile',
    'read_textfile',
    'read_setting',
    'require_python_version',
    'run_command',
    'run_command2',
    'sha1sum',
    'sha256sum',
    'sha384sum',
    'sha512sum',
    'sha3_256sum',
    'sha3_512sum',
    'show_platform',
    'write_jsonfile',
    'DefaultConfig',
    'MyDebug',
    'MyVerbose',
    'WhatNow'
]
