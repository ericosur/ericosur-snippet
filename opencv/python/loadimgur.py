#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
using skimage (scikit-image)
(it will use matplotlib implicitly)
'''

import argparse
import sys

try:
    from skimage import io
except ModuleNotFoundError:
    print('pip install scikit-image')
    sys.exit(1)

from imgconfig import read_image_config

def fetch_image(url, ofn):
    ''' use skimage.io.imread to read an image from URL, may wait a moment '''
    img = io.imread(url)
    io.imsave(ofn, img)
    return img

def load_image(url):
    ''' load image from url '''
    img = io.imread(url)
    return img

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='show an image at imgur')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument('-o', '--output', help='Output file name')

    args = parser.parse_args()

    app_name = 'loadimgur.py'
    data = read_image_config()
    url = data[app_name]['lego']
    print(f'{url=}')

    if args.output:
        ofn = args.output
        print(f'output image to: {ofn}')
        img = fetch_image(url, ofn)
    else:
        img = load_image(url)

    io.imshow(img)
    io.show()


if __name__ == '__main__':
    main()
