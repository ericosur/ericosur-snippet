'''
Module store provides useful utilities and class that helps to query
prime numbers.

'''


# __init__.py

__VERSION__ = '2024.03.27'

from .load_myutil import get_home, GetConfig, read_setting, read_from_stdin
from .store_prime import StorePrime
from .lcp import LoadCompressPrime
from .make_arrow import make_arrow
from .load_myutil import MyDebug, MyVerbose, die
from .load_myutil import is_file, is_dir, prt
from .textutil import read_textfile

def sep():
    ''' sep '''
    print('-------------------------')

__all__ = [
    'die',
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
