#!/usr/bin/env python3
#coding:UTF-8

'''
module segno
'''

import os

import segno


def main():
    ''' main '''
    FN = "hello.png"
    qrcode = segno.make_qr("輸")
    qrcode.save(FN, scale=8)
    cmd = f'zbarimg -q {FN}'
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    main()
