#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' opencv python example '''

from __future__ import print_function
import os
import cv2
import numpy as np
from imgconfig import read_image_config, CONFIG


class OpencvSample():
    ''' run opencv sample '''
    WIN_NAME = 'foobar'
    app_name = 'readim.py'
    RED = (0, 0, 255)
    USE_COLOR = True

    def __init__(self):
        self.data = None
        self.pics = []
        self.img = None
        self._read_config()

    def _read_config(self):
        ''' read config '''
        self.data = read_image_config()
        home = os.environ.get('HOME')
        picpath = os.path.join(home, self.data[self.app_name]['path'])
        print(f'{picpath=}')
        for imgf in self.data[self.app_name]['images']:
            fn = os.path.join(picpath, imgf)
            if os.path.exists(fn):
                self.pics.append(fn)
        if len(self.pics) <= 0:
            print('[INFO] pics list is empty, please check:', CONFIG)

    def demo_drawline(self):
        '''cv drawline'''
        print('draw a diagonal line...')

        (w, h) = (256, 512)
        if self.img is None:
            # Create a black image, notice the h, w position
            img = np.zeros((h, w, 3), np.uint8)
        else:
            img = self.img
            if self.USE_COLOR:
                (w, h, _) = img.shape
            else:
                (w, h) = img.shape
            print(w, h)

        # Draw a diagonal line with thickness of 5 px
        img = cv2.line(img, (w, 0), (0, h), self.RED, 5)    # right-upper to left-lower
        img = cv2.line(img, (0, 0), (w, h), self.RED, 5)    # left-upper to right-lower
        cv2.imshow("line", img)
        cv2.waitKey(0)

    def cv_test(self, fn):
        '''load and show image file'''
        if self.USE_COLOR:
            self.img = cv2.imread(fn, cv2.IMREAD_COLOR)
        else:
            self.img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
        print('press any key to next, showing:', fn)
        cv2.imshow(fn, self.img)
        cv2.waitKey(0)

    def loop_allpics(self):
        ''' loop pics '''
        for f in self.pics:
            self.cv_test(f)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.demo_drawline()
        obj.loop_allpics()
        obj.demo_drawline()
        cv2.destroyAllWindows()

def main():
    '''main function'''
    OpencvSample.run()

if __name__ == '__main__':
    main()
