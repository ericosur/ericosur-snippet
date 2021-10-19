#!/usr/bin/env python3
# coding: utf-8

'''
search radicals from Boshiamy.txt and show unicode code point
'''

import sys
import re
from typing import List
import unicode_blocks

class Solution:
    ''' solution '''
    def __init__(self):
        self.data_file = 'boshiamy_radicals.txt'
        self.fileobj = None
        self.block_obj = unicode_blocks.UnicodeBlock()
        self.lineno = 0

    def __enter__(self):
        #print('__enter__')
        self.fileobj = open(self.data_file, 'rt', encoding='utf8')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        self.fileobj.close()

    def split_line(self, s: str) -> (str, str):
        ''' split line into two part '''
        #print(s)
        arr = s.split(' ')
        if len(arr) != 2:
            print(f'[WARN][{self.lineno}] cannot split into two parts: {s}')
            return (None, None)
        #print(arr)
        return (arr[0], arr[1])

    def show_ans(self, p: str, q: str):
        ''' show answer
        [in] p is the boshiamy radicals
        [in] q is the CJK characters
        '''
        print(f'{p:6s} {q:4s} {ord(q):5X} @{self.lineno} ', end='')
        print(self.block_obj.block(q))


    def find_ch(self, regexp: str):
        ''' find character '''
        print(f'=====> regexp: __{regexp}__')
        self.fileobj.seek(0)
        self.lineno = 0
        for ll in self.fileobj.readlines():
            self.lineno += 1
            (pp, qq) = self.split_line(ll.strip())
            if pp:
                m = re.search(regexp, pp)
                if m:
                    self.show_ans(pp, qq)

def main(argv: List[str]):
    ''' main '''
    with Solution() as s:
        for rr in argv:
            s.find_ch(rr)
            print('*' * 55)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main([r'jzez'])
    else:
        main(sys.argv[1:])
