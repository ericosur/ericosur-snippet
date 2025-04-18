#!/usr/bin/env python3
# coding: utf-8

'''
check if input number is prime or not
may input numbers from CLI and stdin
use 'sympy.ntheory.primetest.isprime()'

eg:
# pick from file
shuf -n 10 prime.txt | python3 check_prime.py -s

# random generate (range from 1001 to 9999)
shuf -i 1001-9999 -n 10 | python3 check_prime.py -s

'''

import argparse
import sys
from random import randint
from store import read_from_stdin
from the_prt import prt
try:
    #from sympy import sympy.ntheory.primetest.isprime
    from sympy import ntheory
except ImportError as err:
    prt('Import Error while:', err)
    sys.exit(1)

def is_prime(n: int):
    ''' check if a prime with sympy '''
    #return sympy.ntheory.primetest.isprime(n)
    return ntheory.primetest.isprime(n)

def gen_large_numbers(size):
    ''' return a list with some large numbers '''
    rets = []
    for _ in range(size):
        n = randint(4222234742, 9999999999)
        rets.append(n)
    return rets

def main(argv: list):
    ''' main '''
    if argv == []:
        prt('>>>>> demo')
        argv.append(7427466391)
        argv.append(1190494759)
        argv.append(4222234741)
        argv.extend(gen_large_numbers(7))

    for e in argv:
        try:
            m = int(e)
            ret = is_prime(m)
            prt(f'{m} is ', end='')
            if ret:
                prt('a PRIME')
            else:
                prt('NOT a prime')
        except ValueError:
            prt('value error:', m)

def argp():
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='check if specified integer is a prime number')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', type=int, default=None)
    args = parser.parse_args()
    #prt(args)
    if args.readFromStdin:
        read_from_stdin(main)
    else:
        main(args.arg)

if __name__ == '__main__':
    argp()
