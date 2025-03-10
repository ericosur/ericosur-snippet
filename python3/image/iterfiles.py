#!/usr/bin/env python3
#coding: utf-8

'''
go through all files under a directory,
check if any spaces in the pathname
'''

import os
import sys
from pathlib import Path
try:
    from loguru import logger  # type: ignore[import]
    logd = logger.debug
except ImportError:
    logd = print

# ruff: noqa: E402
sys.path.insert(0, '.')
sys.path.insert(0, '..')
sys.path.insert(0, 'python3/')
from myutil import prt, get_home  # type: ignore[import]


class Solution():
    ''' class solution '''
    LIMIT = 40
    def __init__(self):
        home = get_home()
        # compose full path
        self.src_dir = os.path.join(home, 'dropbox/Music')
        logd(f'{self.src_dir=}')

    def action(self):
        ''' action '''
        # iterate files under src_dir
        cnt = 0
        for p in Path(self.src_dir).rglob('*'):
            # will break if cnt > LIMIT
            if cnt > self.LIMIT:
                prt(f"too many > {self.LIMIT} directories has space, exit...")
                break
            if not p.is_file():
                if ' ' in str(p):
                    cnt += 1
                    print('[WARN] space in path:', p)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
