#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo percentage encoding, could run both python2, python3
'''


import argparse

from myutil import read_from_stdin

try:
    from urllib.parse import quote
    print('>>>>> using urllib.parse.quote')
except ImportError:
    from urllib import quote
    print('>>>>> using urllib.quote')


def percent_enc(tok):
    ''' print percent encoded string '''
    print(quote(tok.encode("utf-8")))


def show_unicode_escape(cc: str):
    ''' get unicode seq from utf-8 '''
    ue = cc.encode('unicode-escape').decode('utf-8')
    print('unicode-escape:', ue)

#
# The u prefix for strings is no longer necessary in Python >=3.0
#
# for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
# for 00010000 to 0001FFFF, use upper case \U, eg: u'\U00012345'
#
def main(argv):
    '''main function'''
    if argv == []:
        print('>>>>> use predefined tokens...')
        tokens = [
            "\u00A1 \u00BF",
            "\u00C0 \u00C1 \u00C2 \u00C3 \u00C4 \u00C5 \u00C6",
            "\u00E0 \u00E1 \u00E2 \u00E3 \u00E4 \u00E5 \u00E6",
            "\u00C7 \u00C8 \u00C9 \u00CA \u00CB",
            "\u00CC \u00CD \u00CE \u00CF",
            "\u00D0 \u00D1 \u00DD \u00DE",
            "\u00D2 \u00D3 \u00D4 \u00D5 \u00D6 \u00D8",
            "\u00D9 \u00DA \u00DB \u00DC",
            "長度會有變化",
            "长度会有变化",
            "\U0001f648\U0001f649\U0001f64a",
            "\U0001F1F9\U0001F1FC"
        ]
        argv.extend(tokens)

    for tok in argv:
        print(tok)
        percent_enc(tok)
        show_unicode_escape(tok)

def argp():
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='perform percentage encoding on input strings')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', default=None)
    args = parser.parse_args()

    if args.readFromStdin:
        read_from_stdin(main)
        return

    main(args.arg)

if __name__ == '__main__':
    argp()
