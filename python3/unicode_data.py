#!/usr/bin/env python3
# coding: utf-8

'''
example from https://docs.python.org/3/howto/unicode.html
'''

import sys
import unicodedata

def show_unicodedata(u):
    ''' main '''
    for i, c in enumerate(u):
        print('{}: {}  {:04x}  {}'.format(i, c, ord(c), unicodedata.category(c), end=" "))
        print(unicodedata.name(c))
        try:
            # Get numeric value of second character
            print('Numeric character: ', unicodedata.numeric(c))
        except ValueError:
            pass

def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    main(args)

def main(argv):
    ''' main '''
    if argv == []:
        u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231) + chr(33836)
        show_unicodedata(u)
        u = '\u2764\ufe0f'
        show_unicodedata(u)
    else:
        for a in argv:
            show_unicodedata(a)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin()
        else:
            main(sys.argv[1:])
    else:
        # demo mode
        print("demo mode, use '-' to use stdin, or CLI parameters")
        main([])
