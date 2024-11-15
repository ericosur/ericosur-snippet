#!/usr/bin/python3
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

# try to add my code snippet into python path
HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, '/src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

class Solution():
    ''' solution '''
    WORDLIST = 'eff_large_wordlist.txt'

    def __init__(self):
        self.wordfile = None
        self.words = {}
        self.prepare_possible_inputs()
        self.read_data()

    def prepare_possible_inputs(self):
        ''' prepare possible inputs '''
        candicates = []
        _fn = Solution.WORDLIST
        candicates.append(_fn)
        _fn = os.path.join(HOME, Solution.WORDLIST)
        candicates.append(_fn)
        _fn = os.path.join(HOME, 'Downloads', Solution.WORDLIST)
        candicates.append(_fn)
        _fn = os.path.join(HOME, UTILPATH, Solution.WORDLIST)
        candicates.append(_fn)
        for f in candicates:
            if os.path.exists(f):
                self.wordfile = f
                return
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
            r = obj.request_words(randint(3,7))
            print(f'{i}: {r}')

def main():
    ''' main '''
    print('random_string: demo')
    Solution.run()

if __name__ == '__main__':
    main()
