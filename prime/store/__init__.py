'''
Module store provides useful utilities and class that helps to query
prime numbers.

'''

# __init__.py


from .load_myutil import (
    GetConfig,
    MyDebug,
    MyVerbose,
    dbg,
    die,
    do_nothing,
    get_home,
    is_dir,
    is_file,
    prt,
    read_from_stdin,
    read_setting,
)
from .make_arrow import make_arrow
from .store_prime import StorePrime
from .textutil import read_textfile

__VERSION__ = '2024.12.27'
LOCAL_DEBUG = False
dbg = dbg if LOCAL_DEBUG else do_nothing

__all__ = []
try:
    from .lcp import LoadCompressPrime
    __all__.append('LoadCompressPrime')
except ModuleNotFoundError:
    dbg('__init__: cannot load module: LoadCompressPrime')

def sep():
    ''' sep '''
    print('-------------------------')

__all__ = [
    'GetConfig',
    'LoadCompressPrime',
    'MyDebug',
    'MyVerbose',
    'StorePrime',
    'dbg',
    'die',
    'do_nothing',
    'get_home',
    'is_dir',
    'is_file',
    'make_arrow',
    'prt',
    'read_from_stdin',
    'read_setting',
    'read_textfile',
    "sep",
]
