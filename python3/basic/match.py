#!/usr/bin/python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
wrapper to check if python >= 3.10
'''

import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import require_python_version

# pylint: disable=import-outside-toplevel
def main():
    ''' main '''
    major = 3
    minor = 10
    if require_python_version(major, minor) is False:
        print(f'[ERROR] you need python >= {major}.{minor}')
        sys.exit(1)

    # ensure python >= 3.10 then import this
    from match_case import buy
    buy('grape')  # It is purple.
    buy('egg')    # You cannot buy it.

if __name__ == '__main__':
    main()
