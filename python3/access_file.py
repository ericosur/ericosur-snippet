#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""access_file test file existence before using it"""

from __future__ import print_function
import sys
import cv2

# pylint: disable=no-member

def test_file(fn):
    '''
    use open() to test file could be accessed
    '''
    import errno
    try:
        fp = open(fn)
    except IOError as e:
        if e.errno == errno.EACCES:
            print('errno: %s' % 'EACCES')
            return False
        # other than permission error
        if e.errno == errno.ENOENT:
            print('errno: %s' % 'ENOENT')
            return False
        #pass
    else:
        fp.close()
        return True

def main(argv):
    '''
    use cv2.imread() to load an image
    '''
    fn = '/dev/shm/reid.jpg'
    if len(argv) > 1:
        fn = argv[1]
    else:
        print('specify an image file path, using default: %s' % fn)

    if test_file(fn):
        img = cv2.imread(fn)
        cv2.imshow('test', img)
        cv2.waitKey(0)
    else:
        print('main: cannot access file')

if __name__ == '__main__':
    main(sys.argv)
