#!/usr/bin/env python3
# coding: utf-8

'''
read pattern.txt as regexp pattern, and
list files that do not match the pattern
'''

import os
import sys
import re
from glob import glob

USE_ANSICOLOR = False
try:
    from colorama import Fore, Style
    USE_ANSICOLOR = True
except ImportError:
    print('[info] suggest install colorama to enable ansi color')

class Solution:
    ''' check pattern '''
    pat_file = 'pattern.txt'

    def __init__(self):
        self.pat = None
        self.files = []
        self.load_pattern()
        self.noms = []  # pattern not matched files
        self.nofs = []  # file not found files

    def load_pattern(self):
        ''' load pattern from specified file '''
        tmp = None
        with open(self.pat_file, 'rt', encoding='utf-8') as f:
            for ln in f.readlines():
                ln = ln.strip()
                print(ln)
                if len(ln) > 0 and ln[0] != '#':
                    tmp = ln
                    break
        print(f'tmp:$$$ {tmp} $$$')
        self.pat = tmp

    def e(self, msg):
        ''' error message '''
        if USE_ANSICOLOR:
            print(Fore.RED, end='')
        print(msg)
        if USE_ANSICOLOR:
            print(Style.RESET_ALL, end='')

    def w(self, msg):
        ''' warning message '''
        if USE_ANSICOLOR:
            print(Fore.YELLOW, end='')
        print(msg)
        if USE_ANSICOLOR:
            print(Style.RESET_ALL, end='')


    def show_results(self):
        ''' show results '''
        print(f'{len(self.noms)=}')
        if len(self.noms):
            self.w("pattern not match:")
            for f in self.noms:
                self.w(f)
        print(f'{len(self.nofs)=}')
        if len(self.nofs):
            self.e("--file not found:")
            for f in self.nofs:
                self.e(f)

    def do_check(self):
        ''' do check '''
        (tot, nof, nom) = (0, 0, 0)
        for f in self.files:
            tot += 1
            if not os.path.exists(f):
                print('wtf: ', f)
                self.nofs.append(f)
            m = re.match(self.pat, f)
            if not m:
                self.noms.append(f)

    def action(self):
        ''' action '''
        self.files = glob('*.webm')
        self.do_check()
        self.show_results()

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
