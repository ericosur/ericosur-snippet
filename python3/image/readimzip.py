#!/usr/bin/env python3
#coding: utf-8

'''
imageio examples
read image from a zip file, and save to file
'''

import os
from random import randint
import imageio.v3 as iio

class Solution():
    ''' class solution '''
    def __init__(self):
        home = os.getenv('HOME')
        self.zipf = os.path.join(home, 'Pictures/data/mononoke.zip')

    @staticmethod
    def read_from_zip(uri):
        ''' read_oneimg '''
        print(uri)
        #img = iio.imread("path/to/file.zip/abspath/inside/zipfile/to/image.png")
        img = iio.imread(uri)
        return img

    @staticmethod
    def read_from_url(url):
        ''' read from url '''
        print(url)
        img = iio.imread(url)
        return img

    @staticmethod
    def save_to_file(ofn, img):
        ''' save to file '''
        iio.imwrite(ofn, img)
        print('output to:', ofn)

    def action(self):
        ''' action '''
        # download image from URL
        img = self.read_from_url('https://i.imgur.com/VGb6qsV.jpg')
        self.save_to_file('remote.jpg', img)
        # extract image from zip
        RAND = 3
        for _ in range(RAND):
            num = randint(1, 50)
            fn = f'mononoke{num:03d}.jpg'
            fulluri = os.path.join(self.zipf, fn)
            img = self.read_from_zip(fulluri)
            self.save_to_file(fn, img)


    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
