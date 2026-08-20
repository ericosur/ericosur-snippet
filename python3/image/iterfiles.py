#!/usr/bin/env python3

'''
go through all files under a directory,
check if any spaces in the pathname
'''

import os
from pathlib import Path

from image_common import logd, prt  # type: ignore[import]

from myutil import get_home  # type: ignore[import]


class Solution:
    ''' class solution '''
    LIMIT = 40
    def __init__(self):
        # compose full path
        self.src_dir = os.path.join(get_home(), 'dropbox/Music')
        if not os.path.exists(self.src_dir):
            raise ValueError(f"src_dir not exist: {self.src_dir}")
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
            if not p.is_file() and ' ' in str(p):
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
