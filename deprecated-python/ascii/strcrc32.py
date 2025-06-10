#!/usr/bin/python3
# coding: utf-8

''' binascii '''

import binascii

def main():
    ''' main '''
    one = binascii.crc32(b"hello world")
    print('crc1 = 0x%08x' % one)
    # Or, in two pieces:
    two = binascii.crc32(b"hello")
    two = binascii.crc32(b" world", two) & 0xffffffff
    print('crc2 = 0x%08x' % two)

if __name__ == '__main__':
    main()
