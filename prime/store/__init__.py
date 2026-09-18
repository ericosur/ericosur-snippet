'''
Module store provides useful utilities and class that helps to query
prime numbers.

'''

# __init__.py


from .get_config import GetConfig
from .load_myutil import (  # type: ignore[reportAttributeAccessIssue]
    MyDebug,  # type: ignore[reportAttributeAccessIssue]
    MyVerbose,  # type: ignore[reportAttributeAccessIssue]
    dbg,
    die,  # type: ignore[reportAttributeAccessIssue]
    do_nothing,  # type: ignore[reportAttributeAccessIssue]
    get_home,  # type: ignore[reportAttributeAccessIssue]
    import_rich,  # type: ignore[reportAttributeAccessIssue]
    is_dir,  # type: ignore[reportAttributeAccessIssue]
    is_file,  # type: ignore[reportAttributeAccessIssue]
    prime_dir,  # type: ignore[reportAttributeAccessIssue]
    prt,  # type: ignore[reportAttributeAccessIssue]
    read_from_stdin,  # type: ignore[reportAttributeAccessIssue]
    read_setting,  # type: ignore[reportAttributeAccessIssue]
    this_dir,
)
from .make_arrow import make_arrow
from .store_prime import StorePrime
from .textutil import read_textfile

__VERSION__ = '2024.12.27'
LOCAL_DEBUG = False
dbg = dbg if LOCAL_DEBUG else do_nothing

def sep():
    ''' sep '''
    print('-------------------------')

__all__ = [
    'GetConfig',
    'MyDebug',
    'MyVerbose',
    'StorePrime',
    'dbg',
    'die',
    'do_nothing',
    'get_home',
    'import_rich',
    'is_dir',
    'is_file',
    'make_arrow',
    'prime_dir',
    'prt',
    'read_from_stdin',
    'read_setting',
    'read_textfile',
    "sep",
    'this_dir',
]
