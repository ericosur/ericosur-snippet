#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' unicode char test
    could not use python2 to run this
'''

from __future__ import print_function


def main():
    '''main function'''
    STR = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
    arr = list(STR)
    for cc in arr:
        print('cc: {} hex: {}'.format(cc, hex(ord(cc))))

if __name__ == '__main__':
    main()
