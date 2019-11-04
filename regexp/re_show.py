#!/usr/bin/env python3
# coding: utf-8
#

'''
simple show regexp string
'''

import re

def re_show(pat, s):
    ''' show regexp '''
    print(re.compile(pat, re.M).sub(r"{\g<0>}", s.rstrip()), '\n')

def main():
    ''' main '''
    s = '''Mary had a little lamb
And everywhere that Mary
went, the lamb was sure
to go'''

    re_show(r"\w+", s)

if __name__ == '__main__':
    main()
