#!/usr/bin/env python3
#coding: utf-8

'''
imageio x opencv
1. iterate files in specified dir
2. imageio read image file
3. pass image obj to opencv to write image file
'''

# do not complain no-member for opencv
# pylint: disable=no-member
# pylint: disable=import-error

import os
from pathlib import Path

import cv2
import imageio.v3 as iio


class Solution():
    ''' class solution '''
    def __init__(self):
        home = os.getenv('HOME')
        self.src_dir = os.path.join(home, 'Pictures/data')
        self.cnt = 0

    def write_imgfile(self, img):
        ''' use cv2 to write image '''
        ofn = f'imamp{self.cnt:03d}.jpg'
        cv2.imwrite(ofn, img)
        print('[INFO] cv2.imwrite:', ofn)
        self.cnt += 1

    def action(self):
        ''' action '''
        # iterate files under src_dir
        for file in Path(self.src_dir).iterdir():
            if not file.is_file():
                continue
            try:
                # use imageio to read the file as object img
                img = iio.imread(file)
                # need convert RGB to BGR (for cv2)
                new_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                self.write_imgfile(new_img)
            except OSError:
                # handle non-image files
                print('[FAIL] maybe not an valid image: ', file)

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
