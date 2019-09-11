#!/usr/bin/env python3
# utf-8

'''
base64
base85
'''

import base64
from random import randint
import numpy as np

def int_to_bytes(x: int) -> bytes:
    ''' int to bytes '''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    ''' int from bytes '''
    r = int.from_bytes(xbytes, byteorder='big')
    return r

def fill_bytearray(size: int = 24) -> bytes:
    ''' fill byte array '''
    return np.random.bytes(size)


def test(v: bytes):
    ''' test '''
    a = base64.b64encode(v)
    print('base64:', a)
    b = base64.a85encode(v)
    print('base85:', b)


def main(argv):
    ''' main '''
    if argv == []:
        for _ in range(5):
            x = fill_bytearray(randint(16, 48))
            argv.append(x)

    for e in argv:
        try:
            if isinstance(e, str):
                v = e.encode('utf-8')
            elif isinstance(e, int):
                v = int_to_bytes(e)
            elif isinstance(e, bytes):
                v = e
                print('len', len(v))
            else:
                v = bytes(e)
            test(v)
        except ValueError:
            print('invalid input: {}'.format(e))


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
