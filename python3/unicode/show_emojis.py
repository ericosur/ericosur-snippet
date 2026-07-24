#!/usr/bin/env python3
#
# pylint: disable=wrong-import-position

'''
show codepoint from text file (emojis.txt)
also see: ../emoji/test_emoji.py
'''

import sys

sys.path.insert(0, '../emoji/')
try:
    from cp_emoji import EMOJI
except ImportError:
    print("cannot import cp_emoji")
    sys.exit()


class Solution:
    ''' to solve '''
    FILE = "emojis.txt"

    def __init__(self):
        ''' init '''
        self.emojis = EMOJI

    def read_data(self):
        ''' action '''
        print('action!')
        with open(Solution.FILE, "rt", encoding='UTF-8') as fobj:
            for ln in fobj:
                ln = ln.strip()
                self.show_ln(ln)

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
        for cnt, (k, v) in enumerate(self.emojis.items()):
            print(f'{k}: {v}')
            if cnt >= 10:
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
