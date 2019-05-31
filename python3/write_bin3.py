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
    ''' which method is quicker ? '''
    from timeit import timeit
    print(timeit(r'b"\0" * 100'))  # 0.04987576772443264
    print(timeit('bytes(100)'))  # 0.1353608166305015

def fill_bytearray():
    ''' get 1MB byte array '''
    X_1MB = 1024 * 1024
    return np.random.bytes(X_1MB)

def main():
    '''main function'''
    fn = 'write_bin3.bin'
    COUNT = 100 # 100 MB

    with open(fn, 'wb') as binfile:
        for c in range(COUNT):
            barr = fill_bytearray()
            binfile.write(barr)
            print('{}\r'.format(c), end='')

if __name__ == '__main__':
    main()
