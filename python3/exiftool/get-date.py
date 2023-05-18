#!/usr/bin/env python3
# coding: utf-8

'''
demo of module PyExifTool
'''

import os
import re
import sys

try:
    from exiftool import ExifToolHelper
except ImportError:
    print('pip install PyExifTool')
    sys.exit(1)


def extract_gps(fn):
    ''' what '''
    ret = ''
    with ExifToolHelper() as et:
        [exifdata] = et.get_metadata(fn)
        for k in exifdata:
            m = re.search(r'(exif|file).+date', k, re.I)
            if m:
                print(k)

def main():
    ''' main '''
    fn = 'sample.jpg'
    extract_gps(fn)


if __name__ == '__main__':
    main()
