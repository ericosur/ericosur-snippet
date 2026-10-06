#
# pylint: disable=wrong-import-position
#

'''
sample script to import cv2 and list where to load
'''

import os
import sys

import cv2

try:
    from imgconfig import prt, setup_local_paths
    setup_local_paths()
    from myutil import get_python_versions, isdir, isfile
except FileNotFoundError as e:
    print(f'[INFO] file/path not found: {e}')
    sys.exit(1)
except ImportError:
    print('[INFO] no myutil, exit...')
    sys.exit(1)


def main():
    ''' main '''
    prt('python version:', get_python_versions())
    prt('sys version:', sys.version_info)
    prt('opencv version:', cv2.__version__)

    for pp in sys.path:
        target = os.path.join(pp, 'cv2.so')
        #print('check {}'.format(target))
        if isfile(target):
            prt('found cv2.so at ', pp)

        target = os.path.join(pp, 'cv2')
        #print('check {}'.format(target))
        if isdir(target):
            prt('found cv2 at: ', pp)

if __name__ == '__main__':
    main()
