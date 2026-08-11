#!/usr/bin/env python3

'''
bytes to string
string to bytes
'''

import sys

from basic_common import setup_local_paths

try:
    from hexdump import hexdump  # type: ignore[import  ]
    USE_DUMP = True
except ImportError:
    print('no module hexdump need `pip install hexdump`')
    USE_DUMP = False
try:
    setup_local_paths()
    from madlog import get_logd, get_prt
except ModuleNotFoundError:
    print('[INFO] no basic_common or madlog, exit...')
    sys.exit(1)

hexdump = None
USE_LOGURU = True
prt = get_prt()
logd = get_logd(warn_msg="[warn] cannot import loguru", warn_printer=prt, use_loguru=USE_LOGURU)
dump = hexdump if USE_DUMP else print


def b2s(byte_array: bytes) -> str:
    ''' bytes to str '''
    if not isinstance(byte_array, bytes):
        raise TypeError("not a bytes")
    dd = byte_array.decode()
    return dd

def s2b(a_str: str) -> bytes:
    ''' str to bytes array '''
    if not isinstance(a_str, str):
        raise TypeError("not a str")
    b = a_str.encode('UTF-8')
    return b

def test1():
    ''' test 1 '''
    logd('test1...')
    tests = [b'\xef\xa3\xbf', b'\xF0\x9F\x90\xB1']
    for x in tests:
        prt(type(x))
        r = b2s(x)
        prt(type(r), r)

def test2():
    ''' test 2 '''
    logd('test2...')
    s = "特別感謝"
    r = s2b(s)
    prt(type(r))
    dump(r)
    br = bytearray(r)
    prt(type(br))
    dump(br)

def test3():
    ''' test3 '''
    logd('test3...')
    x = bytes(4)
    prt(type(x))
    dump(x)
    y = bytearray(4)
    prt(type(y))
    dump(y)

def main():
    ''' main test function '''
    test2()

if __name__ == '__main__':
    main()
