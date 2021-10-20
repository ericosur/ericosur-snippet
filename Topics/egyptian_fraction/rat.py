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

# Rational: p / q


def get_next(m: int, n: int) -> int:
    ''' get_next '''
    if m > n:
        print(f'm({m}) MUST be smaller than n({n})')
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
        print(f'm{m} MUST be smaller than n{n}')
        sys.exit(1)
    v = Rational(m, n)
    print(f'input: {v}')
    if v.p == 1:
        print(f'{v} is unit fration and stop')
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
    auto_demo = False

    # if values is empty, turn on demo mode automatically
    if len(args.integers) < 2:
        print('Need 2 numbers at least...')
        parser.print_help()
        auto_demo = True
        args.demo = True

    if args.demo:
        print('.....demo.....')
        if not auto_demo and len(args.integers) >= 2:
            print('[INFO] provided values from CLI are ignored...')
        print()

        action(17, 18)
        action(39, 40)
    elif len(args.integers) == 2:
        action(args.integers[0], args.integers[1])

if __name__ == '__main__':
    main()
