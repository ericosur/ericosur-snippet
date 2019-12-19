#!/usr/bin/env python3
# coding: utf-8

'''
example from https://docs.python.org/3/howto/unicode.html
'''

import unicodedata

def show_unicodedata(u):
    ''' main '''
    for i, c in enumerate(u):
        print('{} {} {:04x} {}'.format(i, c, ord(c), unicodedata.category(c), end=" "))
        print(unicodedata.name(c))
        try:
            # Get numeric value of second character
            print('it is a numeric character: ', unicodedata.numeric(c))
        except ValueError:
            pass

def main():
    ''' main '''
    u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231) + chr(33836)
    show_unicodedata(u)
    u = '\u2764\ufe0f'
    show_unicodedata(u)

if __name__ == '__main__':
    main()
