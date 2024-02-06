#!/usr/bin/env python3
# coding: utf-8
#

'''
show codepoint from text file __emojis.txt__
'''

class Solution():
    ''' to solve '''
    FILE = "emojis.txt"

    def __init__(self):
        ''' init '''
        self.chars = []
        self._read_data()

    def _read_data(self):
        ''' action '''
        print('action!')
        with open(Solution.FILE, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                #print(ln)
                ln = ln.strip()
                self.chars.append(ln)

    def action(self):
        ''' action '''
        print(f'{len(self.chars)=}')
        for c in self.chars:
            try:
                print(f'{c}    {hex(ord(c))}')
            except TypeError:
                print(f'error at {c}')


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
