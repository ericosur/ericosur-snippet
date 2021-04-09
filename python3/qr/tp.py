#!/usr/bin/python3.6
# coding: utf-8

'''
require module treepoem

ref: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
'''

import treepoem


def main():
    ''' main '''
    img = treepoem.generate_barcode(
        barcode_type='qrcode',
        data='中文輸入法'
    )

    img.convert('1').save('treepoem.png')


if __name__ == '__main__':
    main()
