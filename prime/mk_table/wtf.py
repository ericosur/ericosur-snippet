#!/usr/bin/env python3
# coding: utf-8

'''
WARNING: NOTICE THAT:

This scripts means to trigger warnings of pylint.
DO NOT FIX warnings from pylint.

Possible warnings:
    - missing-function-docstring
    - consider-using-f-string
    - unreachable
    - wrong-import-order
    - unused-import
'''

import numpy
import argparse

def wtf():
    # here I break some pylint rules
    print('here is the {} print style'.format("old"))
    return
    # here never be executed
    a = 3
    print(a*a/3.141592653589)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("strings", metavar='str', type=str, nargs='*',
        help="show these strings")
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    # define the required args
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    print(args.strings)
    if args.output:
        print('output:', args.output)
    if args.input:
        print('input:', args.input)

    # to show help message directly
    #parser.print_help()

if __name__ == '__main__':
    main()
