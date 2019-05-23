#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
demo to write a binary file
'''

#import binascii
#hs = '5b7f887469feda'
#hb = binascii.a2b_hex(hs)

from __future__ import print_function
import numpy as np

'''
r = random.randint(0, 0xffffffff).to_bytes(4, byteorder='big', signed=False)
'''

def test():
    from timeit import timeit
    print(timeit(r'b"\0" * 100'))  # 0.04987576772443264
    print(timeit('bytes(100)'))  # 0.1353608166305015

def fill_bytearray():
    X_1MB = 1024 * 1024
    return np.random.bytes(X_1MB)

def main():
    '''main function'''
    fn = 'write_bin3.bin'
    COUNT = 100 # 100 MB

    with open(fn, 'wb') as binfile:
        for c in range(COUNT):
            bar = fill_bytearray()
            binfile.write(bar)
            print('{}\r'.format(c), end='')

if __name__ == '__main__':
    main()
