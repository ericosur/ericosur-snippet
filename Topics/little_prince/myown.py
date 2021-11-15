#!/usr/bin/python3
# coding: utf-8

'''
read in __liu.json__
input boshiamy radicals, output characters
'''

from myutil import read_jsonfile

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
