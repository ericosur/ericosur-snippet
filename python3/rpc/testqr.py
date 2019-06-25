#!/usr/bin/env python3
# coding: utf-8

'''
test qrcode generator
'''

import os
from collections import OrderedDict
from urllib.parse import urlencode

import cv2
import requests
#import numpy as np
from httpbin import show_results

# pylint: disable=no-member


def get_qrcode():
    ''' qrcode '''
    # http://goqr.me/api/doc/
    # https://api.qrserver.com/v1/create-qr-code/?data=[URL-encoded-text]&size=[pixels]x[pixels]
    url = 'https://api.qrserver.com/v1/create-qr-code/'
    payload = {
        'data': 'hello world',
        'size': '256x256',
        'ecc': 'M'
    }
    r = requests.get(url, params=payload)
    show_results(r)

class GenerateBarcode():
    ''' barcode: https://github.com/metafloor/bwip-js/wiki/Online-Barcode-API '''
    def __init__(self):
        self.url = 'http://bwipjs-api.metafloor.com/'
        self.resp = None

    def show_resp(self):
        ''' show resp data '''
        fn = show_results(self.resp)
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
        self.resp = requests.get(self.url, params=payload)


    def get_ean13(self, text='4901991570014'):
        ''' generate ean13 barcode '''

        params = OrderedDict(
            [('bcid', 'ean13'), ('text', text), ('scale', 3),
             ('rotate', 'N'), ('includetext', 'null')]
        )
        self.resp = requests.get(self.url, params=urlencode(params))

    def get_isbn(self, text='978-986-137-195-5'):
        ''' generate ean13 barcode '''
        params = OrderedDict(
            [('bcid', 'isbn'), ('text', text), ('scale', 3),
             ('rotate', 'N'), ('includetext', 'null')]
        )
        self.resp = requests.get(self.url, params=urlencode(params))

    @staticmethod
    def show_image(fn):
        '''
        because of returned image with transparent background color,
        this function will replace it into white
        '''
        if not os.path.isfile(fn):
            print('failed to get image:', fn)
            return

        img = cv2.imread(fn, cv2.IMREAD_UNCHANGED)
        if img is None:
            print('failed to read image')
            return

        trans_mask = img[:, :, 3] == 0
        img[trans_mask] = [255, 255, 255, 255]
        new_img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        cv2.imshow('image', new_img)
        cv2.waitKey()


def main():
    ''' main '''
    gen = GenerateBarcode()
    # http://www.otzberg.net/isbn/index.php?isbn=9789861772080
    gen.get_isbn('978-986-177-208-0')
    gen.show_resp()

if __name__ == '__main__':
    main()
