#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
provide funtion show_utf8char()

use this script under python2 only
'''

from __future__ import print_function

def show_utf8char(ch):
    '''show given utf8 char'''
    bc = bytes(ch)
    uch = bc.decode('utf8')
    print(uch)
    print('len: ', len(uch))
    # not work if codepoint > 0xffff
    #print('hex: ', hex(ord(uch)))
    print('uen: ', uch.encode('unicode-escape'))



if __name__ == '__main__':
    show_utf8char('中')
    print()

    S = u' '.join(u"\u037E").encode('utf-8').strip()
    print(f"greek question mark: {S}")
    print()
    cc = ';'
    print(f"char: {cc}\nhex: {ord(cc)}")
