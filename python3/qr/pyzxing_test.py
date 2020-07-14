#!/usr/bin/env python3
# coding: utf-8

'''
pip install pyzxing

It is hard to build my own zxing jar library.
'''

from pyzxing import BarCodeReader
import common


def main():
    ''' main '''
    reader = BarCodeReader()
    for fn in common.get_pngs():
        print('fn:', fn)
        results = reader.decode(fn)
        print(results)

if __name__ == '__main__':
    main()
