#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' opencv python example '''

from __future__ import print_function
import os
import sys
import cv2
import numpy as np
import myutil
#import matplotlib


def cv_drawline():
    '''cv drawline'''
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    # Draw a diagonal blue line with thickness of 5 px
    img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.imshow("foobar", img)
    cv2.waitKey(0)

def cv_test(filename):
    '''load and show image file'''
    #img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("foobar", img)
    cv2.waitKey(0)

def main():
    '''main function'''
    WIN_NAME = 'foobar'
    cv2.namedWindow(WIN_NAME)
    cv2.moveWindow(WIN_NAME, 50, 50)
    if len(sys.argv) > 1:   # has argument
        for ff in sys.argv[1:]:
            print('imread {}'.format(ff))
            img = cv2.imread(ff)
            cv2.imshow(WIN_NAME, img)
            cv2.waitKey(0)
    else:
        setting_fn = 'setting.json'
        if not myutil.isfile(setting_fn):
            print('[ERROR] cannot find setting: {}'.format(setting_fn))
            print('[INFO] may use argument')
        else:
            app_name = 'readim.py'
            data = myutil.read_setting(setting_fn)
            home = os.environ['HOME']
            picpath = home + '/' + data[app_name]['path']
            print(picpath)

        for img_file in data[app_name]['images']:
            pic1 = picpath + '/' + img_file
            print(pic1)
            if not os.path.isfile(pic1):
                print("file not found: {}".format(pic1))
            # else:
            #     cv_test(pic1)

    #cv_drawline()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
