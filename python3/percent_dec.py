#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo percentage decoding
'''

import sys
from myutil import read_from_stdin

try:
    from urllib.parse import unquote
    print('using urllib.parse.quote')
except ImportError:
    from urllib import unquote
    print('using urllib.quote')


def percent_dec(tok: str):
    ''' decode percent encoded string '''
    return unquote(tok, encoding='utf-8')


# def show_unicode_escape(cc: str):
#     ''' get unicode seq from utf-8 '''
#     ue = cc.encode('unicode-escape').decode('utf-8')
#     print('unicode-escape:', ue)



# for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
# for 00010000 to 0001FFFF, use upper case \U, eg: u'\U00012345'
def main(argv):
    '''main function'''
    if argv == []:
        print('use predefined tokens...')
        tokens = [
            '/El%20Ni%C3%B1o/'
        ]
        argv.extend(tokens)

    for inp in argv:
        oup = percent_dec(inp)
        #show_unicode_escape(tok)
        print('input: {}\noutput: {}'.format(inp, oup))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin(main)
        else:
            main(sys.argv[1:])
    else:
        # demo mode
        print('usage: percent_dec.py [arg1] [arg2] ...')
        print('OR from stdin by calling percent_dec.py -\n')
        main([])
