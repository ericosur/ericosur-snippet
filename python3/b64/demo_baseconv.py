#!/usr/bin/env python3
#coding:utf-8

'''
demo of xxx
'''

import base64
from typing import Any

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

from butil import fill_bytearray, sep, int_from_bytes

prt = rprint if USE_RICH else print

# if size = 3k, you will not get padding (the equal sign) after base64
DEFAULT_SIZE = 3*8

def show(m: str, n: Any) -> None:
    ''' show '''
    s = None
    if isinstance(n, bytes):
        s = n.decode('UTF-8')
    elif isinstance(n, str):
        s = n
    else:
        s = str(n)
    prt(f'{m:<16s}: {s}')

def demo(x: Any) -> None:
    ''' demo '''
    msg = x
    if isinstance(x, bytes):
        msg = x.hex()
    prt('demo:', msg)

def bas64(x: bytes) -> None:
    ''' bas64 '''
    e = base64.b64encode(x)
    prt(f'base64: {e!r}')

def main():
    ''' main '''
    prt(f'generate x in size: {DEFAULT_SIZE}')
    x = fill_bytearray(DEFAULT_SIZE)
    prt(f'{x=}')
    bas64(x)
    sep()
    prt('int_from_bytes:', int_from_bytes(x))

if __name__ == "__main__":
    main()
