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
    print('to_from_u8: ue: ' + ue)

def to_utf8(cc: str):
    '''
    get utf-8
    '''
    bb = cc.encode('utf-8')  # bytes
    print('utf-8: ' + bi.b2a_hex(bb).decode())

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

def main():
    ''' main '''
    to_from_u8('Malmö')    # Malm\xf6
    to_from_u8('高畑')    # \u9ad8\u7551
    to_from_u8('🇧🇴')    # \U0001f1e7\U0001f1f4
    to_from_u8('قِبْلَة')    # \u0642\u0650\u0628\u0652\u0644\u064e\u0629

    to_utf8('中文')   # e4b8ade69687
    to_utf8('قِبْلَة')  # d982d990d8a8d992d984d98ed8a9

    # a = b'\xf0\x9f\x98\x80'
    # a.decode('utf-8') # 😀

if __name__ == '__main__':
    main()
