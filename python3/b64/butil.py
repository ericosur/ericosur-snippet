#!/usr/bin/env python3
#codeing:utf-8

'''
some common functions for int/bytes conversion
'''

import numpy as np

def fill_bytearray(size: int = 24) -> bytes:
    ''' fill byte array '''
    return np.random.bytes(size)

def int_to_bytes(x: int) -> bytes:
    ''' int to bytes '''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    ''' int from bytes '''
    r = int.from_bytes(xbytes, byteorder='big')
    return r

def sep():
    ''' print sep '''
    print('-' * 60)
