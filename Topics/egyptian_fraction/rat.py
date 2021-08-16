#!/usr/bin/env python3
# coding: utf-8

'''
need Rational of sympy

* using greedy algorithm to solve egyptian fraction,
  the answer is not always optimized
'''

import argparse
import sys
from sympy import Rational
#from sympy import Float
#from gcd_lcm import gcd_lcm

# Rational: p / q


def get_next(m, n):
    ''' get_next '''
    if m > n:
        print('m MUST be smaller than n')
        sys.exit(1)
    (q, r) = divmod(n, m)
    if r == 0:
        print('something wrong')
        return 0
    return q + 1

# pylint: disable=no-member
def action(m, n):
    ''' action '''
    if m >= n:
        print('{} MUST be smaller than {}'.format(m, n))
        sys.exit(1)
    v = Rational(m, n)
    print('input: {}'.format(v))
    if v.p == 1:
        print('{} is unit fration and stop'.format(v))
        return
    while v.p != 1:
        d = get_next(v.p, v.q)
        nd = Rational(1, d)
        print(nd)
        v = v - nd
    print(v)
    print()

def test(argv):
    ''' main '''
    if argv == []:
        print('.....demo.....')
        action(5, 121)
        action(27, 29)
        return
    try:
        action(int(argv[0]), int(argv[1]))
    except ValueError as e:
        print(e)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='to show an egyptian fraction, m over n')
    parser.add_argument("integers", metavar='ints', type=int, nargs='*',
        help="fractions")

    parser.add_argument("-d", "--demo", action='store_true', default=False,
        help='apply demo values')

    args = parser.parse_args()

    if args.demo:
        print('.....demo.....')
        action(5, 121)
        action(27, 29)
    elif len(args.integers) == 2:
        action(args.integers[0], args.integers[1])
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
