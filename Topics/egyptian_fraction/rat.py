#!/usr/bin/env python3
# coding: utf-8

''' sympy rational '''

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

def main(argv):
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


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('rat.py [p] [q]')
        main([])
        sys.exit(0)

    if len(sys.argv) == 3:
        main(sys.argv[1:])
    else:
        print('need two numbers')

