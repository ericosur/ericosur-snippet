#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
u8u16 tests, apply string directly from CLI or json file
'''

import json
import sys
from logd import logd
from mytofrom import to_from_u8, to_from_u16, to_utf8

sys.path.insert(0, "..")
sys.path.insert(0, "python3")
#print(sys.path)
from myutil import read_jsonfile


def log(*args, **wargs):
    ''' local log, turn of log() by chaning debug to False '''
    logd(*args, **wargs, debug=True)

def common_test(cc):
    ''' common test '''
    to_from_u8(cc)
    to_from_u16(cc)
    ret = to_utf8(cc)
    t = 'to_utf8: '.rjust(16, ' ') + ret
    print(t)

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
    log('test1...')
    arr = [
        '\u2764\ufe0f',
        '\U0001f1e7\U0001f1f4',
        '\U0001f64b\u200d\u2640\ufe0f',
        '\U0001f3c8',
        '\U0001f603'
    ]
    #print(arr)
    payload = {'icons': arr}
    print(json.dumps(payload))
    print()
    #fn = 'out.json'
    #write_json(fn, payload)

def test2():
    ''' test2 '''
    log('test2...')
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
    log('test3...')
    cc = '\U0001f3c8'
    common_test(cc)
    cc = chr(0x0001f603)
    to_from_u16(cc)

def test4():
    ''' test4 '''
    log('test4:')
    cc = '\U0001faa2'
    common_test(cc)


def main(argv: list):
    ''' main '''
    if argv == []:
        #test1()
        #test2()
        #test3()
        test4()
        return

    for s in argv:
        common_test(s)

if __name__ == '__main__':
    main(sys.argv[1:])
