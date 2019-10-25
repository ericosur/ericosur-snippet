#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
show some cjk extension characters
'''


def main():
    '''main function'''
    STR = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
    arr = list(STR)
    for cc in arr:
        print('ch: {} codepoint: {}'.format(cc, hex(ord(cc))))

if __name__ == '__main__':
    main()
