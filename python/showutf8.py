#!/usr/bin/python
# -*- coding: utf-8 -*-

''' provide funtion show_utf8char() '''

from __future__ import print_function

def show_utf8char(ch):
    '''show given utf8 char'''
    uch = ch.decode('utf8')
    print(uch)
    print('len: ', len(uch))
    # not work if codepoint > 0xffff
    #print('hex: ', hex(ord(uch)))
    print('uen: ', uch.encode('unicode-escape'))



if __name__ == '__main__':
    show_utf8char('中')
