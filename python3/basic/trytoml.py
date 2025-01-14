#!/usr/bin/env python3
#coding: utf-8

"""
# try tomllib or tomli

['This parses fine with Python 3.6+']
str = 'the smart fox jumps over the lazy dog'

[main]
filename = "config.toml"
md5sum = "17d802f87cf6704d5bbfaea75bc3c5a8"
"""

import os
import sys

try:
    import tomllib  # type: ignore[import]
except ModuleNotFoundError:
    print('[INFO] no tomllib, exit...')
    sys.exit(1)

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

class Solution():
    ''' class solution '''

    def __init__(self):
        self.value = 0
        prt(f'{sys.version_info=}')

    @staticmethod
    def test():
        ''' test '''
        # parse a long string
        s = tomllib.loads(__doc__)
        prt(s)
        prt()
        # parse a toml file
        fn = s["main"]["filename"]
        if not os.path.exists(fn):
            prt(f'[FAIL] not found: {fn}')
            sys.exit(1)
        with open(fn, "rb") as f:
            s = tomllib.load(f)
        key = 'database'
        prt(f'[INFO] query: {key}')
        for k,v in s[key].items():
            prt(f'{k}: {v}')

    def action(self):
        ''' action '''
        prt('action!')
        Solution.test()

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
