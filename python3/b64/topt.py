#!/usr/bin/env python3
#coding: utf-8

'''
otpauth://totp/GitHub:LarryLuTW?secret=X5CTBOMEYE3TXIIS
'''

import base64

def main():
    ''' main '''
    a: str = 'X5CTBOMEYE3TXIIS'
    print(a)
    r = base64.b32decode(a)
    print(r.hex())

if __name__ == '__main__':
    main()
