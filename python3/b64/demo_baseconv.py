#!/usr/bin/env python3
#coding:utf-8

'''
demo of xxx
'''

import base64
from rich import print as rprint
from butil import fill_bytearray, sep, int_from_bytes

# if size = 3k, you will not get padding (the equal sign) after base64
DEFAULT_SIZE = 3*8

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

def demo(x):
    ''' demo '''
    msg = x
    if isinstance(x, bytes):
        msg = x.hex()
    rprint('demo:', msg)

def bas64(x):
    ''' bas64 '''
    e = base64.b64encode(x)
    rprint(f'base64: {e}')
    sep()

def main():
    ''' main '''
    rprint(f'generate x in size: {DEFAULT_SIZE}')
    x = fill_bytearray(DEFAULT_SIZE)
    rprint(f'{x=}')
    bas64(x)
    rprint('int_from_bytes:', int_from_bytes(x))

if __name__ == "__main__":
    main()
