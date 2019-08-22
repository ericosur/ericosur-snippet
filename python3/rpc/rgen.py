#!/usr/bin/env python3
# coding: utf-8

'''
randomint to base64
add sample of ' Function Annotations'
https://www.python.org/dev/peps/pep-3107/
'''

import binascii as bi
import hashlib
import sys
import numpy as np

def get_random_bytes(size: int = 9) -> bytes:
    '''
    [in] size
    return type: bytes compatible
    '''
    return np.random.bytes(size)

def get_base64(byte_array: bytes) -> bytes:
    '''
    base64 of bytes
    '''
    return bi.b2a_base64(byte_array)

def get_md5(data: bytes) -> str:
    ''' get md5 digest '''
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def get_sha256(data: bytes) -> str:
    ''' get sha256 '''
    m = hashlib.sha256()
    m.update(data)
    return m.hexdigest()

def main(argv: list):
    ''' main test function '''
    if argv == []:
        repeat = 2
        for _ in range(repeat):
            argv.append(get_random_bytes())

    for e in argv:
        if not isinstance(e, bytes):
            b = e.encode('utf-8')
        else:
            b = e
        print('base64:', get_base64(b))
        print('   md5:', get_md5(b))
        print('sha256:', get_sha256(b))
        print()

if __name__ == '__main__':
    main(sys.argv[1:])
