#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
print some unicode char
'''


from __future__ import print_function
from showutf8 import show_utf8char
from myutil import get_python_versions


def main():
    ''' print some unicode characters '''

    # U+F92F (CJK Compatibility Ideographs)
    print('show U+F92F:', '\uF92F')
    # U+52DE (CJK Unified Ideographs)
    print('show U+52DE:', '\u52DE')

    (m, _) = get_python_versions()
    if m >= 3:
        print('[WARN] some functions are obsolete for python3')
        return

    # obsolete: for python3, refer to python3/emoji/mytofrom.py
    #
    # utf8 octets for apple logo (private use area)
    # U+F8FF utf8: EF A3 BF
    a = '\xef\xa3\xbf'
    show_utf8char(a)
    b = '\xF0\x9F\x90\xB1'
    show_utf8char(b)

if __name__ == '__main__':
    main()
