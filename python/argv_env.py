#!/usr/bin/python
# -*- coding: utf-8 -*-
#

'''
    practice for getting environment variables

    The way to get env var:
        os.environ.get('path')
    OR
        os.getenv('path')
'''

from __future__ import print_function
import sys
import os

def main():
    ''' main function '''
    if len(sys.argv) == 1:
        print("usage: %s [arg1] [arg2]..." % sys.argv[0])
        quit()

    for x in range(1, len(sys.argv)):
        if sys.argv[x]:
            en = os.environ.get(sys.argv[x])
        print(sys.argv[x], "=", en)

if __name__ == '__main__':
    main()
