#!/usr/bin/env python3
# coding: utf-8

'''
u8u16 tests, apply string directly from CLI or json file
'''

import sys
import json
from myutil import read_jsonfile
from mytofrom import to_from_u8, to_from_u16, to_utf8

def test0():
    '''
    read emoji from json file
    and print unicode escape sequence
    '''
    fn = 'emj.json'
    print(f'test0, read {fn}')
    data = read_jsonfile(fn)
    if data is None:
        print('failed to read data from json')
        sys.exit()

    # use **string**
    strs = data['string']
    for i, cc in enumerate(strs):
        print('*' * 10, i, '*' * 10)
        to_from_u16(cc)

def test1():
    ''' test1 '''
    arr = [
        u'\u2764\ufe0f',
        u'\U0001f1e7\U0001f1f4',
        u'\U0001f64b\u200d\u2640\ufe0f',
        u'\U0001f3c8',
        u'\U0001f603'
    ]
    #print(arr)
    payload = {'icons': arr}
    print(json.dumps(payload))
    print()
    #fn = 'out.json'
    #write_json(fn, payload)


def test2():
    ''' test2 '''
    s = '漢  χαν  хан'
    #to_from_u8(s)
    to_from_u16(s)
    s = '❤️🇧🇴🙋‍♀️🏈😃'
    #to_from_u8(s)
    to_from_u16(s)
    s = '👨🏻‍🦰'
    to_from_u16(s)

def test3():
    '''
    if I want to get utf-16-be encoding unicode escape, need json.dumps()
    '''
    cc = u'\U0001f3c8'
    to_from_u8(cc)
    to_from_u16(cc)
    cc = chr(0x0001f603)
    to_from_u16(cc)


def main(argv: list):
    ''' main '''
    if argv == []:
        test1()
        #test2()
        #test3()
        sys.exit()

    for s in argv:
        to_from_u16(s)
        to_utf8(s)

if __name__ == '__main__':
    main(sys.argv[1:])
