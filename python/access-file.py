#!/usr/bin/env python2

import cv2
import sys

def test_file(fn):
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
        pass
    else:
        return True

def main(argv):
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
