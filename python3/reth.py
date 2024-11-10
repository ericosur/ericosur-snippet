#!/usr/bin/env python
# coding:utf-8

'''
- rename xxx第2話xxx -> xxx第02話xxx
- battery included
- still need to review or modify the script for different occassion
'''

__VERSION__ = '2024.05.29'

import os
import re
import sys
from glob import glob

def die(*args, **kwargs):
    ''' similar to die in perl '''
    print(*args, file=sys.stderr, **kwargs)
    sys.exit()

class Solution():
    ''' solution '''
    DO_RENAME = True
    TAG = "RETH"
    Debug = True

    def __init__(self):
        self.files = glob('*.webm')
        if len(self.files) == 0:
            die('[info] there is no webm files...')

    def logd(self, *args, **wargs):
        ''' log debug '''
        if self.Debug:
            print(*args, **wargs, file=sys.stderr)

    def is_digits(self):
        ''' is digits '''
        self.logd('is_digits: try normal digit...')
        pairs = []
        self.logd(f'is_digits: {len(self.files)} files...')
        pat1 = r'^(.+)第(\d)話(.+)$'
        pat2 = r'^([^#]+) ?#(\d) (.+)$'
        for f in self.files:
            m = re.match(pat1, f)
            if m:
                self.logd("is_digits: pat1 matched...")
                ep = int(m[2])
                nf = m[1] + '第' + f'{ep:02d}' + '話' + m[3]
                pairs.append((f, nf))
                continue
            m = re.match(pat2, f)
            if m:
                self.logd("is_digits: pat2 matched...")
                ep = int(m[2])
                nf = m[1] + '#' + f'{ep:02d}' + m[3]
                pairs.append((f, nf))
                continue
            self.logd(f'no match: {f}')
        return pairs

    def is_han_digits(self):
        ''' han digits '''
        print('try han digits...')
        s = '○一二三四五六七八九十'
        pairs = []
        for f in self.files:
            ep = 0
            m = re.match(r'^(.+)第(十?)(一|二|三|四|五|六|七|八|九)?話(.+)$', f)
            if m:
                if m[2]=='' and m[3]:
                    ep = s.index(m[3])
                    #print('1st', m[3], ep)
                elif m[2] and m[3] is None:
                    ep = s.index(m[2])
                    #print('2nd', m[2], ep)
                elif m[2] and m[3]:
                    ep = s.index(m[2]) + s.index(m[3])
                    #print('3rd', m[2], m[3], ep)
                nf = m[1] + '第' + f'{ep:02d}' + '話' + m[4]
                pairs.append((f, nf))
        return pairs

    def try_rename(self, pairs):
        ''' try rename '''
        for p in pairs:
            (f, nf) = p
            if self.DO_RENAME:
                os.rename(f, nf)
            print(f'mv {f} {nf}')

    def action(self):
        ''' action '''
        pairs = self.is_digits()
        ret = len(pairs)
        print(f'there are {ret} files matched...')
        self.try_rename(pairs)
        if ret != 0:
            return
        pairs = self.is_han_digits()
        ret = len(pairs)
        print(f'there are {ret} files matched han digits...')
        self.try_rename(pairs)

    @classmethod
    def run(cls):
        ''' runme '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
