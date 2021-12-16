#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
sample script to import cv2 and list where to load
'''

import sys
import cv2
from myutil import isfile, isdir, get_python_version

# pylint: disable=no-member
def main():
    ''' main '''
    print('python version:', get_python_version())
    print('opencv version:', cv2.__version__)

    for pp in sys.path:
        target = pp + '/cv2.so'
        #print('check {}'.format(target))
        if isfile(target):
            print('found cv2.so at ', pp)
        target = pp + '/cv2/'
        #print('check {}'.format(target))
        if isdir(target):
            print('found cv2/ at: ', pp)

if __name__ == '__main__':
    main()
