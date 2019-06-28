#!/usr/bin/env python3
# coding: utf-8

'''
compose url into qrcode
'''

import os
import sys

from testqr import get_qrcode

def main(stockid='4938'):
    ''' main '''
    url = 'https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID={}'.format(stockid)
    print(url)
    get_qrcode(url)

    nfn = 'stock-{}.png'.format(stockid)
    os.rename('image.png', nfn)
    print('rename as', nfn)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        for tt in sys.argv[1:]:
            main(tt)
