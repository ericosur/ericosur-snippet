#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# this script could not run without python2

'''
https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#reading-and-writing-images
'''

# pylint: skip-file

from __future__ import print_function
# using Pillow, not PIL itself
from PIL import Image
from myutil import get_python_version

# http://blog.hardlycode.com/pil-image-from-url-2011-01/
def load_image_from_url(url):
    ''' using stringio to load image from URL '''
    ver = float(get_python_version())
    assert ver < 3.0, 'cannot run under python3'

    import urllib2
    from cStringIO import StringIO
    img_file = urllib2.urlopen(url)
    img = Image.open(StringIO(img_file.read()))
    return img

def save_img(img, fn):
    '''PIL.save()'''
    img.save(fn)

def download_url_to_file(url, fn):
    '''download from url and save to file'''
    ver = float(get_python_version())
    assert ver < 3.0, 'cannot run under python3'

    import urllib2
    from cStringIO import StringIO
    img_url = urllib2.urlopen(url)
    img = Image.open(StringIO(img_url.read()))
    img.save(fn)

def main():
    '''main function'''
    # use imgur direct link
    url = 'https://i.imgur.com/yU4Cbzw.png'
    print('download from: {}'.format(url))
    img = load_image_from_url(url)
    print(img.format, img.size, img.mode)

    #img.show()
    # x1,y1 x2,y2
    box = (200, 80, 600, 560)
    region = img.crop(box)
    region.show()


if __name__ == '__main__':
    main()
