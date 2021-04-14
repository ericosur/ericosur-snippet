#!/usr/bin/env python3
# coding: utf-8

'''
check if input number is prime or not
support read lines from stdin
use 'sympy.ntheory.primetest.isprime()'

eg:
# pick from file
shuf -n 10 prime.txt | python3 check_prime.py -s

# random generate (range from 1001 to 9999)
shuf -i 1001-9999 -n 10 | python3 check_prime.py -s

'''

import argparse
import sys
from myutil import read_from_stdin

def is_prime(n: int):
    ''' check if a prime with sympy '''
    try:
        import sympy
    except ImportError as err:
        print('Import Error while:', err)
        sys.exit(1)
    return sympy.ntheory.primetest.isprime(n)

def main(argv: list):
    ''' main '''
    if argv == []:
        print('>>>>> demo')
        argv.append(7427466391)

    for e in argv:
        try:
            m = int(e)
            ret = is_prime(m)
            print('{} is '.format(m), end='')
            if ret:
                print('a PRIME')
            else:
                print('NOT a prime')

        except ValueError:
            print('value error: {}'.format(m))

def argp():
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='check if specified integer is a prime number')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true', help='read from STDIN')
    parser.add_argument("arg", nargs='*', type=int, default=None)
    args = parser.parse_args()
    #print(args)
    if args.readFromStdin:
        read_from_stdin(main)
    else:
        main(args.arg)


if __name__ == '__main__':
    argp()
