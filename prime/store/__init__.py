'''
Module store provides useful utilities and class that helps to query
prime numbers.

'''

# __init__.py


from .load_myutil import dbg, do_nothing
from .load_myutil import MyDebug, MyVerbose, die
from .load_myutil import is_file, is_dir, prt
from .load_myutil import get_home, GetConfig, read_setting, read_from_stdin
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
    'dbg',
    'die',
    'do_nothing',
    'get_home',
    'is_file',
    'is_dir',
    'GetConfig',
    'LoadCompressPrime',
    'make_arrow',
    'prt',
    'read_from_stdin',
    'read_setting',
    'read_textfile',
    "sep",
    'StorePrime',
    'MyDebug',
    'MyVerbose',
]
