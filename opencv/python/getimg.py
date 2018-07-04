#!/usr/bin/env python2

'''
https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#reading-and-writing-images
'''

from __future__ import print_function
# using Pillow, not PIL itself
from PIL import Image
import urllib2
from cStringIO import StringIO

# http://blog.hardlycode.com/pil-image-from-url-2011-01/
def LoadImageFromUrl(url):
    img_file = urllib2.urlopen(url)
    img = Image.open( StringIO(img_file.read()) )
    return img

def main():
    # use imgur direct link
    url='https://i.imgur.com/yU4Cbzw.png'
    img = LoadImageFromUrl(url)
    print(img.format, img.size, img.mode)
    #img.show()
    # x1,y1 x2,y2
    box = (200, 80, 600, 560)
    region = img.crop(box)
    region.show()

if __name__ == '__main__':
    main()