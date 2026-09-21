#!/usr/bin/env python3

'''
load primes from StorePrime and double check by sympy.isprime
'''

import sys
from time import time

from sympy import isprime  # type: ignore

try:
    from store import GetConfig, StorePrime
except ImportError as e:
    print(f'[FAIL] import error: {e}')
    sys.exit(-1)

MODNAME = "CheckPrimes"
DEFAULT_DATASET = "p1e6"

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3f} sec')

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey(DEFAULT_DATASET)    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    return txtfn, pfn

class CheckPrimes:
    ''' generate a list of numbers and test if a prime number '''

    def __init__(self):
        txtfn, pfn = wrap_config()
        self.sp = StorePrime(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()

    def is_prime(self, val) -> bool:
        ''' is a prime ? '''
        return self.sp.find(val) != -1

    def sympy_prime(self, val) -> bool:
        ''' using sympy '''
        return isprime(val)

    def double_check(self):
        ''' double check by StorePrime and sympy,
            it is very slow
        '''
        CHECK_COUNT = 5_000
        maxidx = self.sp.get_count() - 1
        minidx = max(maxidx - CHECK_COUNT, 0)
        print(f'{maxidx=}')
        start = time()
        for i in range(maxidx, minidx, -1):
            print(f'{i}\r', end='')
            n = self.sp.at(i)
            assert self.is_prime(n)
            assert self.sympy_prime(n)
        print()
        duration = time() - start
        show_duration(duration)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.double_check()

def main():
    ''' main '''
    CheckPrimes.run()

if __name__ == '__main__':
    main()
