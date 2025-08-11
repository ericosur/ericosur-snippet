#!/usr/bin/env python3
# coding: utf-8

'''
read eff wordlist
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
also refer to
https://en.wikipedia.org/wiki/Diceware
'''

import os
import re
import sys
from random import randint
try:
    from rich.console import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print
try:
    sys.path.insert(0, "..")
    from myutil import do_nothing, isfile
except ImportError:
    print('cannot import: myutil.do_nothing')
    sys.exit(1)

DEBUG = True
if not DEBUG:
    logd = do_nothing

class Solution():
    ''' solution '''
    WORDLIST = 'eff_large_wordlist.txt'

    def __init__(self):
        self.words = {}
        try:
            self.wordfile = self.__lookfor_wordlist()
            self.read_data()
        except FileNotFoundError as err:
            print(err)
            sys.exit(1)

    def __lookfor_wordlist(self) -> str:
        ''' look for possible location of word list '''
        home = os.getenv('HOME')
        private = os.path.join(home, "Private")
        downloads = os.path.join(home, 'Downloads')
        utilpath = os.path.join('..', 'myutil')
        possible_paths = ['../data', utilpath, '..', private, downloads, '.']

        for p in possible_paths:
            lookpath = os.path.join(p, Solution.WORDLIST)
            if isfile(lookpath):
                logd(f'path for word list: {lookpath}')
                return lookpath

        print('[ERROR] cannot load WORDLIST')
        raise FileNotFoundError

    def read_data(self) -> None:
        ''' read data '''
        with open(self.wordfile, 'rt', encoding='utf8') as f:
            cnt = 0
            for ln in f.readlines():
                cnt += 1
                m = re.match(r'^(\d+)\s+([a-z-_]+)$', ln)
                if m:
                    self.words[m[1]] = m[2]
                else:
                    print('invalid?', ln)
            if cnt != len(self.words):
                print('[WARN] number of data does not match')

    def rand_words(self) -> str:
        ''' return a random word '''
        idx = ""
        MAX_DIGITS = 5
        for _ in range(MAX_DIGITS):
            idx += str(randint(1, 6))   # simulate a dice
        #print('idx:', idx)
        res = self.words[idx]
        #print('res:', res)
        return res

    def request_words(self, n: int) -> str:
        ''' request words '''
        results = []
        for _ in range(n):
            results.append(self.rand_words())
        res = ' '.join(results)
        res = res.strip()
        return res

    @classmethod
    def run(cls) -> None:
        ''' run demo '''
        obj = cls()
        for i in range(10):
            r = obj.request_words(randint(2,5))
            print(f'{i}: {r}')

if __name__ == '__main__':
    Solution.run()
