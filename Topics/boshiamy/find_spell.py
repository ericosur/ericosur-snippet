#!/usr/bin/env python3
# coding: utf-8

'''
search radicals from Boshiamy.txt and show unicode code point
'''

import sys
import re
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
        self.fileobj = open(self.data_file)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        self.fileobj.close()

    def split_line(self, s):
        ''' split line into two part '''
        #print(s)
        arr = s.split(' ')
        if len(arr) != 2:
            print('[WARN][{}] cannot split into two parts: {}'.format(self.lineno, s))
            return (None, None)
        #print(arr)
        return (arr[0], arr[1])

    def show_ans(self, p, q):
        ''' show answer
        [in] p is the boshiamy radicals
        [in] q is the CJK characters
        '''
        print('{:6s} {:4s} {:5X}  '.format(p, q, ord(q)), end='')
        print(self.block_obj.block(q))


    def find_ch(self, regexp):
        ''' find character '''
        print('=====> regexp: __{}__'.format(regexp))
        self.fileobj.seek(0)
        self.lineno = 0
        for ll in self.fileobj.readlines():
            self.lineno += 1
            (pp, qq) = self.split_line(ll.strip())
            if pp:
                m = re.search(regexp, pp)
                if m:
                    self.show_ans(pp, qq)

def main(argv):
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
