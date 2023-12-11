#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
use sympy to calculate egygtian style of fraction
'''

import argparse
import sys
from typing import List

from read_stdin import read_from_stdin
from sympy import Rational


def sum_fraction(values: List[int]):
    ''' sum of egytian fraction '''
    fracts = [Rational(1, x) for x in values]
    print(f'sum of {fracts}')
    r = sum(fracts)
    print(f'answer: {r}')


def process(argv: List[int]):
    ''' main function '''
    if argv == []:  # no arguments
        print('error: argv must not empty')
        return

    sum_fraction(argv)


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='sum of reciprocal of value array')
    parser.add_argument("values", type=int, nargs='*', help="at least two numbers")
    parser.add_argument('-d', '--demo', action='store_true', default=False,
        help='apply demo values, ignore other inputs')
    parser.add_argument('-s', '--stdin', action='store_true', default=False,
        help='input from stdin, ignore other inputs and arguments even demo')

    args = parser.parse_args()
    auto_demo = False

    if args.stdin:
        print("STDIN mode", '>' * 15, "ctrl-D to interrupt")
        read_from_stdin(process)
        sys.exit(0)

    # if values is empty, turn on demo mode automatically
    if len(args.values) < 2:
        print('Need 2 numbers at least...')
        auto_demo = True
        args.demo = True

    if args.demo:
        print('Demo mode', '>' * 20)
        if not auto_demo and len(args.values) >= 2:
            print('[INFO] provided values from CLI are ignored...')
        # if specified demo, apply the following __arr__
        arr = [6, 12, 15, 20]
        if not auto_demo:
            args.values = arr
        else:
            args.values.extend(arr[:len(arr)-len(args.values)])
    else:
        print('input from cli:', args.values)

    process(args.values)


if __name__ == '__main__':
    main()
