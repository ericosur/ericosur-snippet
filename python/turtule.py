#!/usr/bin/python
# -*- coding: utf-8 -*-

''' unicode char test '''

from __future__ import print_function

def main():
    '''main function'''
    STR = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
    msg = ''
    for cc in list(STR.decode("utf8")):
        #print cc,"\n"
        print(cc, cc.encode('unicode-escape'),)

        for hh in list(cc.encode('utf8')):
            msg += hex(ord(hh)) + ' '

        print(msg)
        msg = ''

if __name__ == '__main__':
    main()
