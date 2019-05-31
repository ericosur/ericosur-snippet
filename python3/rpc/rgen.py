#!/usr/bin/env python3
# coding: utf-8

'''
randomint to base64
'''

from __future__ import print_function
import binascii as bi
import hashlib
import numpy as np

def get_random_bytes(size=64):
    '''
    [in] size
    return type: bytes compatible
    '''
    return np.random.bytes(size)

def get_base64(byte_array):
    '''
    return: type: bytes, in base64
    '''
    return bi.b2a_base64(byte_array)

def get_diget(data):
    '''
    return: str
    '''
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def main():
    ''' main test function '''
    for _ in range(10):
        b = get_random_bytes()
        print(get_base64(b))
        print(get_diget(b))


if __name__ == '__main__':
    main()
