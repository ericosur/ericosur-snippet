#!/usr/bin/env python3
# coding: utf-8

'''
byte array (utf-8 encoding) to a string
'''

from __future__ import print_function

def b2s(byte_array):
    ''' utf-8 decoding '''
    dd = byte_array.decode()
    print(dd)

def main():
    ''' main test function '''
    b2s(b'\xef\xa3\xbf')
    b2s(b'\xF0\x9F\x90\xB1')

if __name__ == '__main__':
    main()
