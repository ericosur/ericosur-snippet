#!/usr/bin/env python3
# coding: utf-8

'''
module binascii example
'''

import binascii


def main():
    ''' main '''
    one = binascii.crc32(b"hello world")
    print(f'crc1 = 0x{one:08x}')
    # Or, in two pieces:
    two = binascii.crc32(b"hello")
    two = binascii.crc32(b" world", two) & 0xffffffff
    print(f'crc2 = 0x{two:08x}')

if __name__ == '__main__':
    main()
