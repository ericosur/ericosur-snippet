#!/usr/bin/env python3
#coding:utf-8

'''
use ImageMagick combine 2 image side-by-side
'''

import os
#import sys
from wand.image import Image
from wand.display import display

class Solution():
    ''' solution '''
    IMAGES = ["IMG_3821.JPEG", "IMG_3822.JPEG"]

    def __init__(self):
        self.ofn = "output.jpg"
        self._check_images()

    def __str__(self):
        return self.ofn

    def _check_images(self):
        ''' check images exists '''
        for f in self.IMAGES:
            if not os.path.exists(f):
                print('[FAIL] fail at once, file not found:', f)

    def test(self, img_file):
        ''' test '''
        with Image(filename=img_file) as img:
            print(img.size)
            for r in 1, 2, 3:
                with img.clone() as i:
                    i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                    i.rotate(90 * r)
                    i.save(filename=f'mona-lisa-{0}.png'.format(r))
                    display(i)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        print(obj)
        obj.test(Solution.IMAGES[0])

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
