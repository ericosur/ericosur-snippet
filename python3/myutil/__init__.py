'''
Module store provides useful utilities

how to export functions
1. import functions from xxxx_util
2. add name of functions into the list: __all__
'''


# __init__.py

__VERSION__ = '2024.11.26'

from .__myutil import get_platform, is_cygwin, is_linux, is_windows
from .commonutil import (
    clamp,
    get_home,
    is_path_exist,
    isdir,
    isfile,
    mkdir,
    print_stderr,
    read_from_stdin,
)
from .debug_verbose import MyDebug, MyVerbose, die, prt
from .hashutil import (
    md5sum,
    sha1sum,
    sha3_256sum,
    sha3_512sum,
    sha256sum,
    sha384sum,
    sha512sum,
)
from .jsonutil import read_jsonfile, read_setting, read_textfile, write_jsonfile
from .mydateutil import get_doom_num, get_dow, get_offset_from_year, is_leapyear
from .pathutil import DefaultConfig
from .queryutil import query_url_for_data, query_url_for_json
from .run_cmd import run_command, run_command2, show_platform
from .thedatetime import WhatNow, get_epoch
from .versionutil import get_python_version, get_python_versions, require_python_version


def sep():
    ''' sep '''
    print('-------------------------')

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return

is_file = isfile
is_dir = isdir

# sort by alphatic if possible
__all__ = [
    'DefaultConfig',
    'MyDebug',
    'MyVerbose',
    'WhatNow',
    'clamp',
    'die',
    'do_nothing',
    'get_doom_num',
    'get_dow',
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
    'read_setting',
    'read_textfile',
    'require_python_version',
    'run_command',
    'run_command2',
    'sha1sum',
    'sha3_256sum',
    'sha3_512sum',
    'sha256sum',
    'sha384sum',
    'sha512sum',
    'show_platform',
    'write_jsonfile'
]
