#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
demo to write a binary file
'''

#import binascii
#hs = '5b7f887469feda'
#hb = binascii.a2b_hex(hs)

from __future__ import print_function
import random

def main():
    '''main function'''
    left_size = 2 ** 20
    s_size = 0
    binfile = open("test.bin", "wb")
    s = ''
    BLOCK_SIZE = 512 * 1024
    while left_size > 0:
        s += "%c" % random.randint(0, 0xff)
        s_size += 1
        if s_size > BLOCK_SIZE:
            binfile.write(s)
            binfile.flush()
            left_size -= s_size
            s_size = 0
            s = ''
            print('left_size: {}'.format(left_size))

    binfile.close()


if __name__ == '__main__':
    main()
