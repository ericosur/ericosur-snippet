#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

'''
天干地支

甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥

'''

from __future__ import print_function

import argparse
import sys

from gngan_yaljux import do_ab, do_tests, do_values, do_verbose

try:
    from rich.console import Console
    console = Console()
    USE_CONSOLE = True
except ImportError:
    print("[WARN] no rich.console to use")
    USE_CONSOLE = False

logd = console.log if USE_CONSOLE else print

def setup_arg_parser():
    ''' setup arg parser '''
    parser = argparse.ArgumentParser(description='script helps to get GanChi, '
                                        'all options will be processed first')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("values", metavar='val', type=int, nargs='*',
        help="show these strings")
    parser.add_argument('-a', '--apple', help='GnGan, 0 < a < 9, a+b mod 2 = 0')
    parser.add_argument('-b', '--ball', help='YalJux, 0 < b < 11, a+b mod 2 = 0')
    parser.add_argument('-c', '--cat', help='center year')
    parser.add_argument("-t", "--test", action='store_true', default=False,
        help='test and demo')
    parser.add_argument("-l", "--list", action='store_true', help='list 天干地支')
    return parser

def main():
    ''' main '''
    parser = setup_arg_parser()
    args = parser.parse_args()

    if args.list:
        if args.values:
            print('[WARN]: will not process specified values:', args.values)
            return
        do_verbose()
        return

    if args.test:
        if args.values:
            print('[WARN]: will not process specified values:', args.values)
            return
        do_tests()
        return

    try:
        if args.apple or args.ball:
            _a = 0
            _b = 0
            if args.apple:
                print('apple:', args.apple)
                _a = int(args.apple)
            if args.ball:
                print('ball:', args.ball)
                _b = int(args.ball)
            do_ab(_a, _b)
            return
    except ValueError:
        print("[ERROR] a or b should be integers, and a+b should be even")
        sys.exit(1)

    if args.values:
        #print(args.values)
        if args.cat:
            do_values(args.values, args.cat)
        else:
            do_values(args.values)
        return

    # to show help message directly
    parser.print_help()

if __name__ == '__main__':
    main()
