#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
percentage encoding / decoding
'''

import sys

try:
    from urllib.parse import quote, unquote
except ImportError as err:
    print('Import error:', err)
    sys.exit(1)


def percent_enc(tok: str) -> str:
    ''' print percent encoded string '''
    return quote(tok.encode("utf-8"))

def percent_dec(tok: str) -> str:
    ''' decode percent decoded string '''
    return unquote(tok, encoding='utf-8')

def show_unicode_escape(cc: str) -> None:
    ''' get unicode seq from utf-8 '''
    ue = cc.encode('unicode-escape').decode('utf-8')
    print('unicode-escape:', ue)

if __name__ == '__main__':
    print('this is a module, not a standalone script')
