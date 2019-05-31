#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
stupid test from code point to char, to utf-8
'''

from __future__ import print_function

def test0(ch):
    ''' show '''
    print('ch: {}, len: {}, hex: {}'.format(ch, len(ch), hex(ord(ch))))
    bb = ch.encode('utf8')
    print('bb: {}, len: {}'.format(bb, len(bb)))
    uu = ch.encode('unicode-escape')
    print('uu: {}'.format(uu))


def test1():
    ''' from 16bit codepint '''
    ss = u'\u037e'
    print("greek question mark: {}    codepoint: {}".format(ss, hex(ord(ss))))
    print("  normal semi colon: {}    codepoint: {}".format(';', hex(ord(';'))))


if __name__ == '__main__':
    CC = '中'
    test0(CC)
    print('----------')
    test1()
