#!/usr/bin/env python3
# encoding: utf-8

'''
byte string into binary
'''

import re

# byte_str [in]: 'e4b8ade69687'
def hex_byte_string_to_codepoint(byte_str: str):
    ''' hex_byte_string_to_codepoint '''
    b = bytes.fromhex(byte_str)
    print('bytes:', b)
    p = b.decode()
    print(p)
    print('len(p):', len(p))
    for cc in p:
        a = hex(ord(cc))
        a = a.replace('0x', 'U+')
        print(a, ':  ', end='')
        print(cc.encode())


def print_simple():
    ''' print_simple '''
    print(chr(0x1f1e7) + chr(0x1f1f4))
    print(chr(0x1f3c8))
    print(chr(0x1f603))


def main():
    ''' main '''

    def sep():
        ''' print seperator '''
        print('-' * 20)

    s = 'e4b8ade69687'  # str
    hex_byte_string_to_codepoint(s)

    sep()
    print_simple()

    print('-' * 20 + 'demo on long hex string' + '-' * 20)
    em = \
    'e2 9d a4 ef b8 8f f0 9f  87 a7 f0 9f 87 b4 f0 9f ' \
    '99 8b e2 80 8d e2 99 80  ef b8 8f f0 9f 8f 88 f0 ' \
    '9f 98 83'
    hex_byte_string_to_codepoint(em)
    sep()

    # a long string that contains extra spaces
    lstr = '''
    e2 9d a4 ef b8 8f f0 9f  87 a7 f0 9f 87 b4 f0 9f
    99 8b e2 80 8d e2 99 80  ef b8 8f f0 9f 8f 88 f0
    9f 98 83
    '''
    # strip() take care head and tail, re.sub() will make extra spaces into one
    sstr = re.sub(r'(\s+)', r' ', lstr.strip())
    print(sstr)
    hex_byte_string_to_codepoint(sstr)


if __name__ == '__main__':
    main()
