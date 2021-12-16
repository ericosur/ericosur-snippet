#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' using skimage (scikit-image) '''

from __future__ import print_function
from skimage import io
import myutil

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
    '''main function'''
    app_name = 'loadimgur.py'
    data = myutil.read_setting('setting.json')
    url = data[app_name]['lego']

    print('url:', url)
    # pylint: disable=using-constant-test
    if False:
        ofn = "output.jpg"
        print(f'url:{url} => {ofn}')
        img = fetch_image(url, ofn)
    else:
        img = load_image(url)

    io.imshow(img)
    io.show()

if __name__ == '__main__':
    main()
