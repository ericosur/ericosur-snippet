#!/usr/bin/python3.6
# coding: utf-8

'''
require module treepoem

ref: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code

online gernerator: https://the-burtons.xyz/barcode-generator/
'''

import argparse
import treepoem
import numpy as np
import cv2

class BarCodeTest():
    def __init__(self, args):
        self.isTemp = False
        if args.output:
            self.output = args.output
        else:
            self.output = '/tmp/treepoem.png'
            self.isTemp = True
        self.verbose = args.verbose
        self.desired_size = 240

    def show_image(self):
        ''' show_image '''
        img = cv2.imread(self.output)
        w, h = img.shape[:2]
        #print(img.shape[:2])
        if w < self.desired_size:
            res = cv2.resize(img, (self.desired_size, self.desired_size), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('treepoem', res)
        cv2.waitKey()

    def generate(self):
        ''' generate '''
        opts = {'eclevel': 'H'}
        img = treepoem.generate_barcode(
            barcode_type='qrcode',
            data='we saw a saw saw a saw',
            options=opts
        )
        img.convert('1').save(self.output)
        if not self.isTemp:
            print('output image: ', self.output)
        if self.verbose:
            self.show_image()

def main():
    ''' main '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="specify output file path")
    parser.add_argument("-v", "--verbose", help="show image", action="store_true")
    args = parser.parse_args()

    bartest = BarCodeTest(args)
    bartest.generate()

if __name__ == '__main__':
    main()
