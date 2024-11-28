#!/usr/bin/env python3
# coding: utf-8

'''
cv2 imshow
'''

import sys
#import numpy as np
import cv2

def show_img(fn):
    ''' show img '''
    img = cv2.imread(fn)
    cv2.imshow('img', img)
    print(f'{fn}: {img.shape[1]}x{img.shape[0]}')
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(argv):
    ''' main '''
    for f in argv:
        show_img(f)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print('please specify file name')
