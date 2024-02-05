#!/usr/bin/env python3
# coding: utf-8

'''
test qrcode generator
'''

# pylint: disable=import-error
import argparse
import os
from collections import OrderedDict
from urllib.parse import urlencode

import requests
#import numpy as np
from httpbin import show_results
from PIL import Image

# pylint: disable=using-constant-test

def get_qrcode(text='The quick brown fox jumps over the lazy dog', showimage=True):
    ''' qrcode '''
    # http://goqr.me/api/doc/
    # https://api.qrserver.com/v1/create-qr-code/?data=[URL-encoded-text]&size=[pixels]x[pixels]
    url = 'https://api.qrserver.com/v1/create-qr-code/'
    payload = {
        'data': text,
        'size': '256x256',
        'ecc': 'M'
    }
    r = requests.get(url, params=payload, timeout=5.0)
    fn = show_results(r)
    if showimage:
        GenerateBarcode.show_image(fn)

class GenerateBarcode():
    ''' barcode: https://github.com/metafloor/bwip-js/wiki/Online-Barcode-API '''
    def __init__(self, showimage=True):
        self.url = 'https://bwipjs-api.metafloor.com/'
        self.resp = None
        self.showimage = showimage

    def show_resp(self):
        ''' show resp data '''
        if self.resp is None:
            return
        fn = show_results(self.resp)
        if fn is None:
            return
        if self.showimage:
            self.show_image(fn)

    def get_code128(self, text='AB1234567890'):
        ''' code 128 '''
        payload = {
            'bcid': 'code128',
            'text': text,
            'scale': 3,
            'rotate': 'N',
            'includetext': 'null'
        }
        self.resp = requests.get(self.url, params=payload, timeout=5.0)

    def get_ean13(self, text='4901991570014'):
        ''' generate ean13 barcode '''
        params = OrderedDict(
            [('bcid', 'ean13'), ('text', text), ('scale', 3),
             ('rotate', 'N'), ('includetext', 'null')]
        )
        self.resp = requests.get(self.url, params=urlencode(params),
                                    timeout=5.0)

    def get_isbn(self, text='978-986-137-195-5'):
        ''' generate ean13 barcode '''
        if text.find('-') < 0:
            print('[get_isbn] need add proper hypen in ISBN')
            return
        params = OrderedDict(
            [('bcid', 'isbn'), ('text', text), ('scale', 3),
             ('rotate', 'N'), ('includetext', 'null')]
        )
        self.resp = requests.get(self.url, params=urlencode(params),
                                    timeout=5.0)

    @staticmethod
    def show_image(fn):
        ''' show image '''
        if fn is None or not os.path.isfile(fn):
            print('failed to get image:', fn)
            return
        image = Image.open(fn)
        image.show()

    # pylint: disable=import-outside-toplevel
    @staticmethod
    def show_image_cv2(fn, fillbackground=True):
        '''
        because of returned image with transparent background color,
        this function will replace it into white
        '''
        import cv2
        img = cv2.imread(fn, cv2.IMREAD_UNCHANGED)
        if img is None:
            print('failed to read image')
            return

        if fillbackground:
            trans_mask = img[:, :, 3] == 0
            img[trans_mask] = [255, 255, 255, 255]
            new_img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        else:
            new_img = img

        cv2.imshow('image', new_img)
        cv2.waitKey()


def do_isbn(arg, showimage=True):
    ''' test '''
    print('isbn:', arg)
    gen = GenerateBarcode(showimage)
    # help to hypenate isbn
    # http://www.otzberg.net/isbn/index.php?isbn=9789861772080
    gen.get_isbn(arg)
    gen.show_resp()

def do_urls(args, showimage=True):
    '''
    text = 'https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=4938'
    '''
    for t in args:
        get_qrcode(t, showimage)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='use web API to generate barcode')
    parser.add_argument("urls", nargs='*', help='qrcode')
    parser.add_argument("--isbn", nargs='?', help='ISBN need hypenated, eg: 978-986-998-168-2')
    parser.add_argument("-v", "--verbose", action='store_true', default=True,
        help='show resp results')
    parser.add_argument("-s", "--showimage", action='store_true', help='show generated image')
    args = parser.parse_args()

    if args.isbn:
        do_isbn(args.isbn, args.showimage)
    elif args.urls:
        do_urls(args.urls, args.showimage)
    else:
        print('no aruments provided, use --help to see')

if __name__ == '__main__':
    main()
