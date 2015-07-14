#!/usr/bin/python
# -*- coding: utf-8 -*-

def showutf8(ch):
    uch = ch.decode('utf8')
    print uch
    print 'len: ', len(uch)
    # not work if codepoint > 0xffff
    #print 'hex: ', hex(ord(uch))
    print 'uen: ', uch.encode('unicode-escape')
    print
