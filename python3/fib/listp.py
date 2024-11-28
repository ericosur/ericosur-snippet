#!/usr/bin/env python3
# coding: utf-8
#
'''
use pickle to load
'''

import pickle
import sys

try:
    from sympy import ntheory
except ImportError as err:
    print('Import Error while:', err)
    sys.exit(1)

def is_prime(n):
    ''' use sympy.ntheory to test primes '''
    return ntheory.primetest.isprime(n)

def load_pickle(fn):
    ''' load pickle file '''
    mydata = {}
    UPPER = 1_500_000
    try:
        with open(fn, "rb") as fh:
            mydata = pickle.load(fh)
            for k,v in mydata.items():
                if v > UPPER:
                    break
                print(f'{k}\t{v}', end='')
                if is_prime(v):
                    print('\tis PRIME')
                else:
                    print()
    except IOError as e:
        print('IOError:', e)

def main():
    ''' main '''
    load_pickle('fib.p')

if __name__ == '__main__':
    main()
