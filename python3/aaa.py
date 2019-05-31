#!/usr/bin/env python3
# coding: utf-8

'''
unicode zjw test
'''

from __future__ import print_function

def main():
    ''' main test '''
    # MUST NOT edit the following string if your editor/system
    # could not handle this correctly
    s = '❤️🇧🇴🙋‍♀️🏈😃'
    #line = '"'
    for cc in s:
        hx = hex(ord(cc))  # str, 0x1f1e7

        hx = hx.upper()
        hx = hx.replace('0X', '\\u')
        print(hx)

        print(cc.encode())

    #line += '"'
    #print(line)

if __name__ == '__main__':
    main()
