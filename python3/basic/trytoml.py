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
    import tomllib
except ModuleNotFoundError:
    print('[INFO] no tomllib, try tomli')
    try:
        import tomli as tomllib
    except ModuleNotFoundError:
        print('[INFO] use: pip install tomli')

class Solution():
    ''' class solution '''

    def __init__(self):
        self.value = 0
        print(f'{sys.version_info=}')

    @staticmethod
    def test():
        ''' test '''
        # parse a long string
        s = tomllib.loads(__doc__)
        print(s)
        print()
        # parse a toml file
        fn = s["main"]["filename"]
        if not os.path.exists(fn):
            print(f'[FAIL] not found: {fn}')
            sys.exit(1)
        with open(fn, "rb") as f:
            s = tomllib.load(f)
        key = 'database'
        print(f'[INFO] query: {key}')
        for k,v in s[key].items():
            print(f'{k}: {v}')

    def action(self):
        ''' action '''
        print('action!')
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
