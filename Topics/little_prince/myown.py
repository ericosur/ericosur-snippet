#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
read in __liu.json__
input boshiamy radicals, output characters
'''

import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile


class Bosha:
    ''' read liu.json and rad.txt output han characters '''
    DATA_JSON = 'liu.json'

    def __init__(self, fn: str):
        self.fn = fn
        self.data = read_jsonfile(self.DATA_JSON)

    def action(self):
        ''' main flow '''
        if not self.data:
            print("[FAIL] cannot load data json:", self.DATA_JSON)
            sys.exit(1)
        cdefs = self.data["chardefs"]
        print(f'cdefs size: {len(cdefs)}')
        with open(self.fn, 'rt', encoding='utf-8') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                chars = ln.split(' ')
                for c in chars:
                    if c == '':
                        continue
                    try:
                        r = cdefs[c]
                        ans = r[0]
                        print(f'{ans}', end='\u2003')
                    except KeyError as e:
                        print(f'Spelling not found: [{e}]')
                        print()
                print()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls('rad.txt')
        obj.action()

def main():
    ''' main '''
    Bosha.run()

if __name__ == '__main__':
    main()
