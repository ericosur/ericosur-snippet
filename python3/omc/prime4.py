#!/usr/bin/python3
# coding: utf-8

'''
0, 1, 2, 3
three-digit number is prime
'''

import itertools as it
import sys

try:
    #from sympy import sympy.ntheory.primetest.isprime
    from sympy import ntheory
except ImportError as err:
    print('Import Error while:', err)
    sys.exit(1)

def is_prime(n):
    ''' true if n is a prime number '''
    return ntheory.primetest.isprime(n)

def test_prime():
    ''' test_prime '''
    vals = [41, 43, 45, 47, 49, 71, 97]
    for n in vals:
        if is_prime(n):
            print(f'{n} is prime')

def make_num_and_test(ii):
    ''' compose a number and test if a prime '''
    n = 100 * ii[0] + 10 * ii[1] + ii[2]
    if n < 100:  # not 3-digit number
        return False
    if is_prime(n):
        print(f'{n} is prime')
        return True
    return False

def test_comb():
    ''' test comb '''
    digits = range(4)
    for ii in it.permutations(digits, 3):
        make_num_and_test(ii)


def main():
    ''' main '''
    print('main')
    test_comb()

if __name__ == '__main__':
    main()
