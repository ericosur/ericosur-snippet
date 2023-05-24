#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=no-member

'''some cv util functions'''


from __future__ import print_function
import os
import sys
import cv2
import numpy

__version__ = '0.0,1'

def translate_img_to_str(fn):
    '''
    read image from **fn**
    and return stringData as image byte array
    '''
    img = cv2.imread(fn)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, img_str = cv2.imencode('.jpg', img, encode_param)
    if result:
        #print('img_str: {}'.format(img_str))
        data = numpy.array(img_str)
        stringData = data.tostring()
        return stringData

    print('failed to imencode')
    return ""


def combine_two_images(ofn, inf1, inf2, debug=False):
    '''
    specify inf1, and inf2, combine these two images horizontally
    if image height are not the same, will resize to max one and then
    combine

    refer from:
    https://stackoverflow.com/questions/7589012/combining-two-images-with-opencv

    '''
    img1 = cv2.imread(inf1)
    img2 = cv2.imread(inf2)

    # maybe I should use min() instead of max()?
    new_height = max(img1.shape[0], img2.shape[0])
    new_width = max(img1.shape[1], img2.shape[1])

    if debug:
        print('img1:', img1.shape)
        print('img2:', img2.shape)
        print(f'===> combine_two_images: fn:{inf1} fn:{inf2}')
        print(f'new height:{new_height}, new width:{new_width}')

    #if img1.shape[0] != new_height or img1.shape[1] != new_width:
    img1 = cv2.resize(img1, (new_width, new_height))

    #if img2.shape[0] != new_height or img2.shape[1] != new_width:
    img2 = cv2.resize(img2, (new_width, new_height))

    # axis = 1, left is img1, and right is img2
    # need have same height
    vis = numpy.concatenate((img1, img2), axis=1)
    cv2.imwrite(ofn, vis)



def main():
    '''main function'''

    # strData = translate_img_to_str('lena.jpg')
    # print strData
    ofn = 'out.jpg'
    if len(sys.argv) == 1:
        fn1 = 'img1.jpg'
        fn2 = 'img2.jpg'
        debug = False
    elif len(sys.argv) == 3:
        fn1 = sys.argv[1]
        fn2 = sys.argv[2]
        debug = True
    else:
        print('specify img1 img2...')
        return

    if os.path.exists(fn1) and os.path.exists(fn2):
        combine_two_images(ofn, fn1, fn2, debug)
        print('output to:', ofn)
    else:
        print(f'{fn1} and/or {fn2} is not available')

if __name__ == '__main__':
    main()
