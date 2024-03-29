#!/usr/bin/python3
# coding: utf-8


'''
wrapper to check if python >= 3.10
'''

import os
import sys

sys.path.insert(0, "../")
from myutil import require_python_version


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
