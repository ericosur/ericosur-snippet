#!/usr/bin/env python3
# coding: utf-8

'''
unicode zjw test
'''

def show_code(s):
    ''' show code '''
    for cc in s:
        hx = hex(ord(cc))  # str, 0x1f1e7

        hx = hx.upper()
        hx = hx.replace('0X', '\\u')
        print(f'{cc:8s}{hx:12s}{cc.encode()}')

def main():
    ''' main test '''
    # MUST NOT edit the following string if your editor/system
    # could not handle this correctly
    s = '❤️🇧🇴🙋‍♀️🏈😃'
    print(s)
    show_code(s)

    s = '龍龖龘' + '\U0002A6A5'
    print(s)
    show_code(s)

if __name__ == '__main__':
    main()
