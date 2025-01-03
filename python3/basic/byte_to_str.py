#!/usr/bin/env python3
# coding: utf-8

'''
bytes to string
string to bytes
'''

try:
    from rich import print as rprint
    from loguru import logger
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

try:
    from hexdump import hexdump  # type: ignore[import  ]
    USE_DUMP = True
except ImportError:
    print('need install module hexdump')
    #sys.exit(1)
    USE_DUMP = False

def nothing(*_args, **_kwargs) -> None:
    ''' do donothing'''
    return None

logd = logger.debug if USE_RICH else nothing
dump = hexdump if USE_DUMP else nothing


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
