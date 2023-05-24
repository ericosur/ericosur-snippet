#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' split image into multiple channels '''

from __future__ import print_function
import os
import sys
import cv2 as cv
import numpy as np
from imgconfig import read_image_config

# pylint: disable=no-member

THUMBNAIL_HEIGHT = 300
THUMBNAIL_WIDTH = 300

def output_img(fn, img):
    ''' imshow specified image file '''
    #print("output to: {}".format(fn))
    #cv.imwrite(fn, img)
    cv.imshow(fn, img)

def preprocess(src):
    ''' resize image and minus mean value '''
    img = cv.resize(src, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    img = img - 127.5
    #img = img * 0.007843
    return img

def apply_mean(src):
    ''' apply some mean values '''
    img = cv.resize(src, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    b, g, r = cv.split(img)
    #104,117,123
    b = np.subtract(b, 104)
    g = np.subtract(g, 117)
    r = np.subtract(r, 123)
    #zeros = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
    img = cv.merge([b, g, r])
    return img

def setup_windows():
    ''' setup showing windows '''
    cv.namedWindow('red')
    cv.moveWindow('red', 0, 0)
    cv.namedWindow('green')
    cv.moveWindow('green', THUMBNAIL_WIDTH, 0)
    cv.namedWindow('blue')
    cv.moveWindow('blue', THUMBNAIL_WIDTH * 2, 0)
    cv.namedWindow('merged.png')
    cv.moveWindow('merged.png', 0, THUMBNAIL_HEIGHT+50)
    cv.namedWindow('preproc.png')
    cv.moveWindow('preproc.png', THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT+50)


def split_and_show(img):
    ''' split into multiple channels and show '''
    img = cv.resize(img, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    b, g, r = cv.split(img)
    zeros = np.zeros(img.shape[:2], dtype=img.dtype)
    cv.imshow('red', cv.merge([zeros, zeros, r]))
    cv.imshow('blue', cv.merge([b, zeros, zeros]))
    cv.imshow('green', cv.merge([zeros, g, zeros]))

def main():
    '''main function'''
    app_name = 'split.py'
    data = read_image_config()

    home = os.environ["HOME"]
    image = os.path.join(home, data[app_name]['image_file'])

    if not os.path.exists(image):
        print("image not found:", image)
        sys.exit(1)

    setup_windows()

    img = cv.imread(image)
    split_and_show(img)

    mrg = apply_mean(img)
    output_img('merged.png', mrg)

    newimg = preprocess(img)
    output_img('preproc.png', newimg)

    print('press any key to quit...')
    cv.waitKey()
    # When everything done, release the capture
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
