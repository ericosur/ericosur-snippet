#!/usr/bin/python

# -*- coding: big5 -*-
# notice now this file is stored as ansi text

def print_hex(in_string):
    for c in list(s):
        print("%X" % ord(c), end=' ')
    print()


s = "¤¤¤å¦r"   # notice the prefix 'u'
print(s)
print_hex(s)    # would print the unicode code point
print(s.encode('utf-8'))
print_hex(s)

# -*- coding: utf-8 -*-
# the text file nned to be stored in utf-8
