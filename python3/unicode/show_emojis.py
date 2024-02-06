#!/usr/bin/env python3
# coding: utf-8
#

'''
show codepoint from text file (emojis.txt)
'''

import sys
sys.path.insert(0, '../emoji/')

from cp_emoji import EMOJI


class Solution():
    ''' to solve '''
    FILE = "emojis.txt"

    def __init__(self):
        ''' init '''
        self.emojis = EMOJI

    def read_data(self):
        ''' action '''
        print('action!')
        with open(Solution.FILE, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                self.show_ln(ln)
                r = self.emojis.get(ln)

    def show_ln(self, ln):
        ''' show ln '''
        r = self.emojis.get(ln)
        if len(ln) == 1:
            print(f'{ln}: {hex(ord(ln))}, {r}')
        else:
            msg = ''
            for ch in list(ln):
                msg = msg + f'/{hex(ord(ch))}/'
            print(f'{ln}: {msg}  {r}')


    def action(self):
        ''' action '''
        self.read_data()

    def test(self):
        ''' test '''
        print('run test...')
        cnt = 0
        for k in self.emojis.keys():
            v = self.emojis[k]
            print(f'{k}: {v}')
            cnt += 1
            if cnt > 10:
                break

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main() -> None:
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
