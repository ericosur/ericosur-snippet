#!/usr/bin/python
# -*- coding: big5 -*-

'''
notice now this file is stored as ansi text
'''

from __future__ import print_function

def print_hex(in_string):
    ''' print string in hex '''
    for c in list(in_string):
        print("%X" % ord(c), end=' ')
    print()


STR = "中文字"   # notice the prefix 'u'
print(STR)
print_hex(STR)    # would print the unicode code point
print(STR.encode('utf-8'))
print_hex(STR)

# -*- coding: utf-8 -*-
# the text file nned to be stored in utf-8
