#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
stupid test from code point to char, to utf-8
'''

from __future__ import print_function


def test0(ch):
    ''' show '''
    print(f'ch: {ch}, len: {len(ch)}, hex: {hex(ord(ch))}')
    bb = ch.encode('utf8')
    print(f'bb: {bb}, len: {len(bb)}')
    uu = ch.encode('unicode-escape')
    print(f'uu: {uu}')


def test1():
    ''' from 16bit codepint '''
    # The u prefix for strings is no longer necessary in Python >=3.0
    ss = '\u037e'
    print(f"greek question mark: {ss}    codepoint: {hex(ord(ss))}")
    n1 = ';'
    print(f"  normal semi colon: {n1}    codepoint: {hex(ord(n1))}")


if __name__ == '__main__':
    CC = '中'
    test0(CC)
    print('----------')
    test1()
