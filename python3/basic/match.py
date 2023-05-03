#!/usr/bin/python3
# coding: utf-8

'''
wrapper to check if python >= 3.10
'''

import sys
from myutil import require_python_version

# pylint: disable=import-outside-toplevel
def main():
    ''' main '''
    if require_python_version(3, 10) is False:
        print('[ERROR] you need python >= 3.10')
        sys.exit(1)

    # ensure python >= 3.10 then import this
    from match_case import buy
    buy('grape')  # It is purple.
    buy('egg')    # You cannot buy it.

if __name__ == '__main__':
    main()
