#!/usr/bin/env python3
#codeing:utf-8
# pylint: disable=invalid-name

'''
demo for the following base-N functions:
    base58
    base64
    base85

reference: https://docs.python.org/zh-tw/3/library/base64.html
'''

from typing import Any
import base64
import sys

try:
    import base58  # type: ignore[import]
    USE_B85 = True
except ImportError:
    print('WARN: cannot import module: base58', file=sys.stderr)
    USE_B85 = False

try:
    from rich.console import Console
    console = Console()
except ImportError:
    print('INFO: no rich.console available')

from butil import fill_bytearray, sep, int_to_bytes

def is_py310plus() -> bool:
    ''' return python version in (major, minor) integers '''
    return sys.version_info[0]==3 and sys.version_info[1]>=10

def show(m: str, n: Any) -> None:
    ''' show '''
    s = None
    if isinstance(n, bytes):
        s = n.decode('UTF-8')
    elif isinstance(n, str):
        s = n
    else:
        s = str(n)
    print(f'{m:<16s}: {s}')

def demo58(v: bytes) -> None:
    ''' base 58 '''
    if not USE_B85:
        return
    r = base58.b58encode(v)
    show('base58', r)
    sep()

def demo85(v: bytes) -> None:
    ''' test base85 '''
    r = base64.a85encode(v) # r is bytes
    show('base85a', r)
    r = base64.b85encode(v) # r is bytes
    show('base85b', r)
    sep()

def demo64(v: bytes) -> None:
    ''' demo base64 '''
    b0 = base64.standard_b64encode(v)
    b1 = base64.b64encode(v)
    b2 = base64.urlsafe_b64encode(v)

    if b0 != b1:
        show('std base64', b0)
    show('base64', b1)
    if b1 != b2:
        show('urlsafe base64', b2)
    sep()

# pylint: disable=no-member
def demo32(v: bytes) -> None:
    ''' demo base32 '''
    show("base32", base64.b32encode(v))
    if is_py310plus():
        show("base32hex", base64.b32hexencode(v))
    sep()

def test(v: bytes) -> None:
    ''' test '''
    #hx = binascii.hexlify(v)    # bytes: b'([0-9a-f][0-9a-f])+'
    #show('input', hx)
    hxx = v.hex()               # str: ([0-9a-f][0-9a-f])+
    show('input hex', hxx)
    #b16 = base64.b16encode(v)   # bytes: b'([0-9A-F][0-9A-F])+'
    #show('b16encode', b16)
    sep()
    # base32
    demo32(v)
    # base58
    demo58(v)
    # base64
    demo64(v)
    # base85
    demo85(v)

def main(argv):
    ''' main '''
    DEFAULT_SIZE = 19
    if argv == []:
        for _ in range(1):
            x = fill_bytearray(DEFAULT_SIZE)
            show("size", DEFAULT_SIZE)
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
