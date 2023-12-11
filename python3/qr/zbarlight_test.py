#!/usr/bin/env python3
# coding: utf-8

'''
apt-get install libzbar-dev
pip install zbarlight

I do not recomment use this module to decode qrcode.
'''

import sys

import common
from PIL import Image

try:
    import zbarlight
except ImportError:
    print('need to install zbarligt (python) and libzbar-dev')
    sys.exit(1)


def read_image(fn):
    ''' read image '''
    im = None
    with open(fn, "rb") as fin:
        im = Image.open(fin)
        im.load()
    return im


def process():
    ''' process '''
    arr = common.get_pngs()
    for fn in arr:
        print('fn:', fn)
        im = read_image(fn)
        codes = zbarlight.scan_codes(['qrcode'], im)
        # codes in type 'byte'
        for s in codes:
            print(s)
            print(s.decode('utf-8'))


def main():
    ''' main '''
    process()

if __name__ == '__main__':
    main()
