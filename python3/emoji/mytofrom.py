#!/usr/bin/env python3
# coding: utf-8

'''
unicode escape sequence to utf-8 and backward
'''

import json
import binascii as bi

__version__ = '0.1'

def to_from_u8(cc: str):
    '''
    get unicode seq from utf-8
    '''
    ue = cc.encode('unicode-escape').decode('utf-8')
    #print('to_from_u8: ue: ' + ue)
    return ue

def to_utf8(cc: str):
    '''
    get utf-8
    '''
    bb = cc.encode('utf-8')  # bytes
    ret = bi.b2a_hex(bb).decode()
    #print('utf-8: ' + ret)
    return ret

def to_from_u16(cc: str):
    '''
    cc [in] unicode char
    calling: to_from_u16(chr(0x0001f3c8))
    '''
    print('         input: ' + cc)
    ue = cc.encode('unicode-escape').decode('utf-8')
    u16s = json.dumps(cc).replace('"', '')
    print('unicode-escape: ' + ue)
    print('      utf16-be: ' + u16s)

def from_utf8char(cc):
    ''' old show_utf8char for python 3 '''
    ret = None
    if isinstance(cc, bytes):
        ret = cc.decode('utf-8')
    else:
        raise ValueError("need input bytes")
    return ret

def demo(src, dst):
    ''' demo '''
    print(src, "=>", dst)

def main():
    ''' main '''

    print("demo to_from_u8()...\n")
    strs = [
        'Malmö',  # Malm\xf6
        '高畑',    # \u9ad8\u7551
        '🇧🇴',     # \U0001f1e7\U0001f1f4
        'قِبْلَة'    # \u0642\u0650\u0628\u0652\u0644\u064e\u0629
    ]
    for s in strs:
        demo(s, to_from_u8(s))

    print("\ndemo to_utf8()...\n")
    strs = [
        '中文',   # e4b8ade69687
        'قِبْلَة'  # d982d990d8a8d992d984d98ed8a9
    ]
    for s in strs:
        demo(s, to_utf8(s))

    print('\nhow to decode utf-8 byte sequence ?')
    # define a byte array which is utf-8, and then decode it
    a = b'\xf0\x9f\x98\x80'  # 😀
    c = from_utf8char(a)
    print(a, c)

    # a utf-8 like str, convert it to bytearray with encoding
    a = '\xef\xa3\xbf'
    b = bytearray(a, 'utf-8')
    print(a, b)
    c = from_utf8char(bytes(b))
    print(c)

    # b = '\xF0\x9F\x90\xB1'
    # show_utf8char(b)

if __name__ == '__main__':
    main()
