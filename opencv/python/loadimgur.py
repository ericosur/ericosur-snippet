#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' using skimage (scikit-image) '''

from __future__ import print_function
from skimage import io
import myutil

def main():
    '''main function'''
    app_name = 'loadimgur.py'
    data = myutil.read_setting('setting.json')
    url = data[app_name]['lego']
    print('url:{}'.format(url))

    # use skimage.io.imread to read an image from URL, may wait a moment
    img = io.imread(url)
    io.imshow(img)
    io.show()


if __name__ == '__main__':
    main()
