#!/usr/bin/env python3
# coding: utf-8

'''
simply to show how to import a module within another sub-directory
'''

import emoji.mytofrom

def main():
    ''' main '''
    s = '中文'

    emoji.mytofrom.to_utf8(s)
    print()
    emoji.mytofrom.to_from_u8(s)
    print()
    emoji.mytofrom.to_from_u16(s)

if __name__ == '__main__':
    main()
