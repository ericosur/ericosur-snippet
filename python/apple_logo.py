#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''print some unicode char'''


from __future__ import print_function
from showutf8 import show_utf8char


def main():
    ''' print some unicode characters '''
    # utf8 octets for apple logo (private use area)
    # U+F8FF utf8: EF A3 BF
    a = '\xef\xa3\xbf'
    show_utf8char(a)

    b = '\xF0\x9F\x90\xB1'
    show_utf8char(b)

    # U+F92F (CJK Compatibility Ideographs)
    print('show U+F92F:', u'\uF92F')

    # U+52DE (CJK Unified Ideographs)
    print('show U+52DE:', u'\u52DE')


if __name__ == '__main__':
    main()
