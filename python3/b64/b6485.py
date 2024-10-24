#!/usr/bin/env python3
# utf-8

'''
demo for the following base-N functions:
    base58
    base64
    base85

reference: https://docs.python.org/zh-tw/3/library/base64.html
'''

import base64
import sys
from random import randint
import numpy as np

USE_B85 = False
try:
    import base58
    USE_B85 = True
except ImportError:
    print('WARN: cannot import module: base58', file=sys.stderr)


def is_py310plus() -> bool:
    ''' return python version in (major, minor) integers '''
    return sys.version_info[0]==3 and sys.version_info[1]>=10

def int_to_bytes(x: int) -> bytes:
    ''' int to bytes '''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    ''' int from bytes '''
    r = int.from_bytes(xbytes, byteorder='big')
    return r

def fill_bytearray(size: int = 24) -> bytes:
    ''' fill byte array '''
    show("size", size)
    return np.random.bytes(size)

def show(m, n):
    ''' show '''
    s = None
    if isinstance(n, bytes):
        s = n.decode('UTF-8')
    elif isinstance(n, str):
        s = n
    else:
        s = str(n)
    print(f'{m:<16s}: {s}')

def demo85(v: bytes):
    ''' test base85 '''
    print('-' * 60)
    r = base64.a85encode(v) # r is bytes
    show('base85a', r)
    r = base64.b85encode(v) # r is bytes
    show('base85b', r)
    if USE_B85:
        print('-' * 60)
        r = base58.b58encode(v)
        show('base58', r)

def demo64(v: bytes):
    ''' demo base64 '''
    b0 = base64.standard_b64encode(v)
    b1 = base64.b64encode(v)
    b2 = base64.urlsafe_b64encode(v)

    if b0 != b1:
        show('std base64', b0)
    show('base64', b1)

    if b1 != b2:
        show('urlsafe base64', b2)

def demo32(v: bytes):
    ''' demo base32 '''
    show("base32", base64.b32encode(v))
    if is_py310plus():
        show("base32hex", base64.b32hexencode(v))

def test(v: bytes):
    ''' test '''
    #hx = binascii.hexlify(v)    # bytes: b'([0-9a-f][0-9a-f])+'
    #show('input', hx)
    hxx = v.hex()               # str: ([0-9a-f][0-9a-f])+
    show('input hex', hxx)
    #b16 = base64.b16encode(v)   # bytes: b'([0-9A-F][0-9A-F])+'
    #show('b16encode', b16)
    print('-' * 60)
    # base32
    demo32(v)
    # base64
    demo64(v)
    # base85
    demo85(v)


def main(argv):
    ''' main '''
    if argv == []:
        for _ in range(1):
            x = fill_bytearray(19)
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
            print(f'invalid input: {e}')


if __name__ == '__main__':
    main(sys.argv[1:])
