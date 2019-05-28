#!/usr/bin/env python3
# coding: utf-8

import os
import json
import myutil

def test0():
    '''
    read emoji from json file
    '''
    fn = 'emj.json'
    data = myutil.read_jsonfile(fn)
    icons = data['icons']
    if not icons:
        os.exit(1)
    print(icons)

def test1():
    arr = [u'\u2764\ufe0f', u'\U0001f1e7\U0001f1f4',
        u'\U0001f64b\u200d\u2640\ufe0f', u'\U0001f3c8', u'\U0001f603'
    ]
    #print(arr)
    payload = {'icons': arr}
    print(json.dumps(payload))
    fn = 'out.json'
    myutil.write_json(fn, payload)

def to_from(s):
    encoding = 'utf-8'
    print('unicode: ' + s.encode('unicode-escape').decode(encoding))
    u = s.encode('unicode-escape').decode(encoding)
    print('str: ' + u.encode(encoding).decode('unicode-escape'))
    #u = r'\u6f22  \u03c7\u03b1\u03bd  \u0445\u0430\u043d'
    #print('str: ' + u.encode("utf-8").decode('unicode-escape'))


def to_from_u8(cc):
    ue = cc.encode('unicode-escape').decode('utf-8')
    print('to_from_u8: ue: ' + ue)

def to_from_u16(cc):
    '''
    cc [in] unicode char

    calling: to_from_u16(chr(0x0001f3c8))
    '''
    ue = cc.encode('unicode-escape').decode('utf-8')
    u16s = json.dumps(cc).replace('"','')
    print('unicode-escape: ' + ue)
    print('utf16-be: ' + u16s)

def test2():
    s = '漢  χαν  хан'
    to_from_u8(s)
    to_from_u16(s)
    s = '❤️🇧🇴🙋‍♀️🏈😃'
    to_from_u8(s)
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


def main():
    #test2()
    test3()

if __name__ == '__main__':
    main()
