#!/usr/bin/env python3
# coding: utf-8

'''
load primes from StorePrime and double check by nthoery
'''

import sys
from time import time
from sympy import ntheory

try:
    from store import GetConfig, StorePrime
except ImportError as e:
    print(f'[FAIL] import error: {e}')
    sys.exit(-1)

MODNAME = "CheckPrimes"

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3f} sec')

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("small")    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    return txtfn, pfn

class CheckPrimes():
    ''' generate a list of numbers and test if a prime number '''

    def __init__(self):
        txtfn, pfn = wrap_config()
        self.sp = StorePrime(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()

    def is_prime(self, val):
        ''' is a prime ? '''
        return self.sp.find(val) != -1

    def sympy_prime(self, val):
        ''' using sympy '''
        return ntheory.primetest.isprime(val)

    def double_check(self):
        ''' double check by StorePrime and sympy,
            it is very slow (1e5 numbers takes 22 seconds)
        '''
        maxidx = self.sp.get_count() - 1
        print(f'{maxidx=}')
        start = time()
        for i in range(maxidx, 0, -1):
            print(f'{i}\r', end='')
            n = self.sp.at(i)
            assert self.is_prime(n)
            assert self.sympy_prime(n)
        print()
        duration = time() - start
        show_duration(duration)

    def action(self):
        ''' action '''
        self.double_check()

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    CheckPrimes.run()

if __name__ == '__main__':
    main()
