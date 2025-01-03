#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo percentage decoding
'''

import argparse
from myutil import read_from_stdin
from percent_encdec import percent_dec


# for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
# for 00010000 to 0001FFFF, use upper case \U, eg: u'\U00012345'
def main(argv):
    '''main function'''
    if argv == []:
        print('>>>>> use predefined tokens...')
        tokens = [
            '/El%20Ni%C3%B1o/'
        ]
        argv.extend(tokens)

    for inp in argv:
        oup = percent_dec(inp)
        #show_unicode_escape(tok)
        print(f'input: {inp}\noutput: {oup}')

def argp() -> None:
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='perform percentage encoding on input strings')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', default=None)
    args = parser.parse_args()
    #print(args)

    if args.readFromStdin:
        read_from_stdin(main)
        return

    main(args.arg)

if __name__ == '__main__':
    argp()
