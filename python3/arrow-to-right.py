#!/usr/bin/env python3
# coding: utf-8

'''
just try to know if a is a multi-char string
'''

def main():
    ''' main '''
    a='→'
    for c in list(a):
        print(c)
        print('codepoint:',ord(c))

if __name__ == '__main__':
    main()
