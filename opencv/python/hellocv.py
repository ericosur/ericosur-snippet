#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# pylint: disable=wrong-import-position

'''
sample script to import cv2 and list where to load
'''

import os
import sys
import cv2

HOME = os.getenv('HOME')
#UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
#if os.path.exists(UTILPATH):
sys.path.insert(0, '../../python3')

from myutil import isfile, isdir, get_python_versions


def main():
    ''' main '''
    print('python version:', get_python_versions())
    print('opencv version:', cv2.__version__)

    for pp in sys.path:
        target = os.path.join(pp, 'cv2.so')
        #print('check {}'.format(target))
        if isfile(target):
            print('found cv2.so at ', pp)

        target = os.path.join(pp, 'cv2')
        #print('check {}'.format(target))
        if isdir(target):
            print('found cv2 at: ', pp)

if __name__ == '__main__':
    main()
