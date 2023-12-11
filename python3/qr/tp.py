#!/usr/bin/python3
# coding: utf-8

'''
require module treepoem

ref: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code

online gernerator: https://the-burtons.xyz/barcode-generator/
'''

import argparse

#import numpy as np
import cv2
import treepoem


class BarCodeTest():
    ''' class barcode test '''
    def __init__(self, args):
        self.is_temp = False
        if args.output:
            self.output = args.output
        else:
            self.output = '/tmp/treepoem.png'
            self.is_temp = True
        self.content = args.str1
        self.verbose = args.verbose
        self.desired_size = 240

    def show_image(self):
        ''' show_image '''
        img = cv2.imread(self.output)
        w, _ = img.shape[:2]
        #print(img.shape[:2])
        if w < self.desired_size:
            res = cv2.resize(img, (self.desired_size, self.desired_size), \
                interpolation=cv2.INTER_CUBIC)
        cv2.imshow('treepoem', res)
        cv2.waitKey()

    def generate(self):
        ''' generate '''
        opts = {'eclevel': 'H'}
        img = treepoem.generate_barcode(
            barcode_type='qrcode',
            data=self.content,
            options=opts
        )
        img.convert('1').save(self.output)
        if self.is_temp and not self.verbose:
            print('output temp:', self.output)
        if not self.is_temp:
            print('output image:', self.output)
        if self.verbose:
            self.show_image()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='Encode specified string into qrcode image')
    parser.add_argument("str1", help="will encode this string into qrcode")
    parser.add_argument("-o", "--output", help="specify output file path")
    parser.add_argument("-v", "--verbose", help="show image", action="store_true")
    args = parser.parse_args()

    bartest = BarCodeTest(args)
    bartest.generate()

if __name__ == '__main__':
    main()
