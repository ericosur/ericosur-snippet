#!/usr/bin/env python3
# utf-8

'''
base58
base64
base85
'''

import base64
from random import randint
import base58
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

    def show(m, n):
        ''' show '''
        print('{:<14s}: {}'.format(m, n))

    #hx = binascii.hexlify(v)    # bytes: b'([0-9a-f][0-9a-f])+'
    #show('input', hx)
    hxx = v.hex()               # str: ([0-9a-f][0-9a-f])+
    show('input hex', hxx)
    #b16 = base64.b16encode(v)   # bytes: b'([0-9A-F][0-9A-F])+'
    #show('b16encode', b16)
    print('-' * 60)

    r0 = base64.standard_b64encode(v)
    r1 = base64.b64encode(v)
    r2 = base64.urlsafe_b64encode(v)

    if r0 != r1:
        show('std base64', r0)
    show('base64', r1)

    if r1 != r2:
        show('urlsafe base64', r2)

    print('-' * 60)
    r = base64.a85encode(v)
    show('base85a', r)
    r = base64.b85encode(v)
    show('base85b', r)

    print('-' * 60)
    r = base58.b58encode(v)
    show('base58', r)


def main(argv):
    ''' main '''
    if argv == []:
        for _ in range(1):
            x = fill_bytearray(randint(10, 40))
            argv.append(x)

    for e in argv:
        try:
            if isinstance(e, str):
                v = e.encode('utf-8')
            elif isinstance(e, int):
                v = int_to_bytes(e)
            elif isinstance(e, bytes):
                v = e
            else:
                v = bytes(e)

            test(v)
            print()
        except ValueError:
            print('invalid input: {}'.format(e))


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
