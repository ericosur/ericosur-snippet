#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo percentage encoding, could run both python2, python3
'''

import sys
from myutil import read_from_stdin

try:
    from urllib.parse import quote
    print('using urllib.parse.quote')
except ImportError:
    from urllib import quote
    print('using urllib.quote')


def percent_enc(tok):
    ''' print percent encoded string '''
    print(quote(tok.encode("utf-8")))


def show_unicode_escape(cc: str):
    ''' get unicode seq from utf-8 '''
    ue = cc.encode('unicode-escape').decode('utf-8')
    print('unicode-escape:', ue)


# for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
# for 00010000 to 0001FFFF, use upper case \U, eg: u'\U00012345'
def main(argv):
    '''main function'''
    if argv == []:
        print('use predefined tokens...')
        tokens = [
            u"\u00A1 \u00BF",
            u"\u00C0 \u00C1 \u00C2 \u00C3 \u00C4 \u00C5 \u00C6",
            u"\u00E0 \u00E1 \u00E2 \u00E3 \u00E4 \u00E5 \u00E6",
            u"\u00C7 \u00C8 \u00C9 \u00CA \u00CB",
            u"\u00CC \u00CD \u00CE \u00CF",
            u"\u00D0 \u00D1 \u00DD \u00DE",
            u"\u00D2 \u00D3 \u00D4 \u00D5 \u00D6 \u00D8",
            u"\u00D9 \u00DA \u00DB \u00DC",
            u"長度會有變化",
            u"长度会有变化",
            u"\U0001f648\U0001f649\U0001f64a",
            u"\U0001F1F9\U0001F1FC"
        ]
        argv.extend(tokens)

    for tok in argv:
        print(tok)
        percent_enc(tok)
        show_unicode_escape(tok)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin(main)
        else:
            main(sys.argv[1:])
    else:
        # demo mode
        print('usage: percent_enc.py [arg1] [arg2] ...')
        print('OR from stdin by calling percent_enc.py -')
        main([])
