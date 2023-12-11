#!/usr/bin/env python3
#coding:utf-8

'''
use ImageMagick combine 2 image side-by-side

cli:
magick montage \
    lhs.png rhs.png \
    -mode Concatenate -tile x1 \
    output.png

For **wand**, you need to install ImageMagick runtime library into system as well
libmagickwand

reference: https://imagemagick.org/Usage/

'''

DEMO = False

import os
import sys

from wand.display import display
from wand.image import Image


class Solution():
    ''' solution '''

    def __init__(self):
        home = os.getenv("HOME")
        self.images = ["padlock1.png", "padlock2.png"]
        self.src_dir = os.path.join(home, 'Pictures/data')
        self.ofn = "output.png"
        self._check_images()

    def __str__(self):
        return self.ofn

    def _check_images(self):
        ''' check images exists '''
        self.fullpaths = [os.path.join(self.src_dir, f) for f in self.images]
        for f in self.fullpaths:
            if not os.path.exists(f):
                print('[FAIL] fail at once, file not found:', f)
                sys.exit(-1)

    def concatenate_images(self):
        ''' concatenate images
        https://docs.wand-py.org/en/0.6.12/guide/montage.html#concatenation-mode
        '''
        with Image() as img:
            for src in self.fullpaths:
                with Image(filename=src) as item:
                    img.image_add(item)
                    img.montage(mode='concatenate')
                    #img.border('magenta', 2, 2)
                    img.save(filename=self.ofn)
        print('concatenate_images: output to:', self.ofn)

    def rotate_and_show(self):
        ''' rotate and show '''
        with Image(filename=self.fullpaths[0]) as img:
            print(img.size)
            # resize and rotate
            for r in 1, 2, 3:
                with img.clone() as i:
                    i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                    i.rotate(90 * r)
                    #i.save(filename=f'mona-lisa-{r}.png')
                    display(i)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        if DEMO:
            print('[INFO] press ESC or close the display window to next one')
            obj.rotate_and_show()
        else:
            obj.concatenate_images()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
