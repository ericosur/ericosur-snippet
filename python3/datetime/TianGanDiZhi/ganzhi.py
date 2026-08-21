#!/usr/bin/env python3
# pylint: disable=invalid-name

'''
天干地支

甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥

'''


import argparse
import sys

from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
from tgdz_common import do_nothing, logd


def setup_arg_parser():
    ''' setup arg parser '''
    parser = argparse.ArgumentParser(description='script helps to get GanChi, '
                                        'all options will be processed first')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("values", metavar='val', type=int, nargs='*',
        help="show these strings")
    parser.add_argument('-a', '--apple', type=int, help='GnGan 天干, 0 <= a <= 9, a+b mod 2 = 0')
    parser.add_argument('-b', '--ball', type=int, help='YalJux 地支, 0 <= b <= 11, a+b mod 2 = 0')
    parser.add_argument('-c', '--context', '--cat', type=int, default=0,
        help='show years within this radius around each specified year')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
        help='turn on debug log')
    parser.add_argument("-t", "--test", action='store_true', default=False,
        help='test and demo')
    parser.add_argument("-l", "--list", action='store_true', help='list 天干地支')
    return parser

def main():
    ''' main '''
    parser = setup_arg_parser()
    args = parser.parse_args()
    _logd = logd if args.debug else do_nothing

    if args.list:
        if args.values:
            print('[WARN]: will not process specified values:', args.values)
            return
        do_verbose(_logd=_logd)
        return

    if args.test:
        if args.values:
            print('[WARN]: will not process specified values:', args.values)
            return
        do_tests(_logd=_logd)
        return

    try:
        if args.apple is not None or args.ball is not None:
            _a = 0
            _b = 0
            if args.apple is not None:
                _a = args.apple
            if args.ball is not None:
                _b = args.ball
            do_ab(_a, _b, radius=args.context, _logd=_logd)
            return
    except ValueError:
        print("[ERROR] a or b should be integers, and a+b should be even")
        sys.exit(1)

    if args.values:
        #print(args.values)
        do_values(args.values, radius=args.context, _logd=_logd)
        return

    # to show help message directly
    parser.print_help()

if __name__ == '__main__':
    main()
