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
from .debug_verbose import MyDebug, MyVerbose, die
from .hashutil import md5sum, sha1sum, sha256sum
from .jsonutil import read_setting, read_textfile, read_jsonfile, write_jsonfile
from .mydateutil import get_dow, is_leapyear, get_offset_from_year, get_doom_num
from .pathutil import DefaultConfig
from .queryutil import query_url_for_data, query_url_for_json
from .thedatetime import get_epoch, WhatNow
from .versionutil import get_python_version, get_python_versions, require_python_version
from .__myutil import is_linux, is_cygwin, is_windows, get_platform

def sep():
    ''' sep '''
    print('-------------------------')

is_file = isfile
is_dir = isdir

# sort by alphatic if possible
__all__ = [
    'clamp',
    'die',
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
    'query_url_for_data',
    'query_url_for_json',
    'read_from_stdin',
    'read_jsonfile',
    'read_textfile',
    'read_setting',
    'require_python_version',
    'sha1sum',
    'sha256sum',
    'write_jsonfile',
    'DefaultConfig',
    'MyDebug',
    'MyVerbose',
    'WhatNow'
]
