'''
Module store provides useful utilities
'''


# __init__.py

__VERSION__ = '2024.03.28'

from .commonutil import get_home, print_stderr, read_from_stdin
from .commonutil import is_path_exist, isfile, isdir
from .debug_verbose import MyDebug, MyVerbose
from .hashutil import md5sum, sha1sum, sha256sum
from .jsonutil import read_setting, read_textfile, read_jsonfile, write_jsonfile
from .queryutil import query_url_for_data, query_url_for_json
from .versionutil import get_python_version, get_python_versions, require_python_version

def sep():
    ''' sep '''
    print('-------------------------')


# sort by alphatic if possible
__all__ = [
    'get_home',
    'get_python_version',
    'get_python_versions',
    'is_path_exist',
    'isfile',
    'isdir',
    'md5sum',
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
    'MyDebug',
    'MyVerbose',
]
