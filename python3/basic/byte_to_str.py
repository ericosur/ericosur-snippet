#!/usr/bin/env python3
# coding: utf-8

'''
bytes to string
string to bytes
'''

from __future__ import print_function

import sys

try:
    from hexdump import hexdump
except ImportError:
    print('need install module hexdump')
    sys.exit(1)

def b2s(byte_array):
    ''' bytes to str '''
    if not isinstance(byte_array, bytes):
        raise TypeError("not a bytes")
    dd = byte_array.decode()
    return dd

def s2b(a_str):
    ''' str to bytes array '''
    if not isinstance(a_str, str):
        raise TypeError("not a str")
    b = a_str.encode('UTF-8')
    return b

def test1():
    ''' test 1 '''
    tests = [b'\xef\xa3\xbf', b'\xF0\x9F\x90\xB1']
    for x in tests:
        print(type(x))
        r = b2s(x)
        print(type(r), r)

def test2():
    ''' test 2 '''
    s = "特別感謝"
    r = s2b(s)
    print(type(r))
    hexdump(r)
    br = bytearray(r)
    print(type(br))
    hexdump(br)

def test3():
    ''' test3 '''
    x = bytes(4)
    print(type(x))
    hexdump(x)
    y = bytearray(4)
    print(type(y))
    hexdump(y)


def main():
    ''' main test function '''
    test2()

if __name__ == '__main__':
    main()
