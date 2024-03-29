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
from .debug_verbose import MyDebug, MyVerbose

def sep():
    ''' sep '''
    print('-------------------------')

__all__ = [
    'get_home',
    'GetConfig',
    'LoadCompressPrime',
    'make_arrow',
    'read_from_stdin',
    'read_setting',
    "sep",
    'StorePrime',
]
