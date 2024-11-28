#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
show some cjk extension characters
'''


def main():
    '''main function'''
    STR = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
    for cc in list(STR):
        print(f'ch: {cc} codepoint: {ord(cc)}')

if __name__ == '__main__':
    main()
