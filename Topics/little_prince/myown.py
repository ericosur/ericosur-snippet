#!/usr/bin/python3
# coding: utf-8

'''
read in __liu.json__
input boshiamy radicals, output characters
'''

import os
import json

def read_jsonfile(fn, debug=False):
    '''
    specify json filename and return whole json object
    '''
    if debug:
        print(f'load json from {fn}')
    if not os.path.exists(fn):
        print('file not found')
        return None

    # read from json file
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)
    return data

class Bosha:
    ''' read liu.json and rad.txt output han characters '''
    json_fn = 'liu.json'
    def __init__(self, fn: str):
        self.fn = fn
        self.data = None

    def action(self):
        ''' main flow '''
        self.data = read_jsonfile(self.json_fn)
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

def main():
    ''' main '''
    bs = Bosha('rad.txt')
    bs.action()

if __name__ == '__main__':
    main()
