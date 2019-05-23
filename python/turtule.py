#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function


def main():
    '''main function'''
    STR = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
    arr = list(STR)
    for cc in arr:
        print('ch: {} codepoint: {}'.format(cc, hex(ord(cc))))

if __name__ == '__main__':
    main()
