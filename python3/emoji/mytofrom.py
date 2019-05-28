#!/usr/bin/env python3
# coding: utf-8

import json
import binascii as bi

def to_from_u8(cc):
    ue = cc.encode('unicode-escape').decode('utf-8')
    print('to_from_u8: ue: ' + ue)

def to_utf8(cc):
    bb = cc.encode('utf-8')  # bytes
    print('utf-8: ' + bi.b2a_hex(bb).decode())

def to_from_u16(cc):
    '''
    cc [in] unicode char

    calling: to_from_u16(chr(0x0001f3c8))
    '''
    print(cc)
    ue = cc.encode('unicode-escape').decode('utf-8')
    u16s = json.dumps(cc).replace('"','')
    print('unicode-escape: ' + ue)
    print('utf16-be: ' + u16s)

__version__ = '0.1'
