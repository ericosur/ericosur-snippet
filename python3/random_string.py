#!/usr/bin/python3.6
# coding: utf-8

'''
read eff wordlist
'''

import os
import re
from random import randint
import sys

HOME = os.getenv('HOME')
UTILPATH = HOME + '/src/ericosur-snippet/python3'
sys.path.insert(0, UTILPATH)
#import myutil

class Solution():
    ''' solution '''
    def __init__(self):
        #self.wordfile = HOME + '/Downloads/eff_large_wordlist.txt'
        self.wordfile = UTILPATH + '/eff_large_wordlist.txt'
        self.words = dict()
        self.read_data()

    def read_data(self):
        ''' read data '''
        with open(self.wordfile, 'rt') as f:
            cnt = 0
            for ln in f.readlines():
                cnt += 1
                m = re.match(r'^(\d+)\s+([a-z-_]+)$', ln)
                if m:
                    self.words[m[1]] = m[2]
                else:
                    print('invalid?', ln)
            #print('read {} lines'.format(cnt))
            #print('len:', len(self.words))
            if cnt != len(self.words):
                print('[WARN] number of data does not match')

    def rand_words(self):
        ''' return a random word '''
        idx = ""
        MAX_DIGITS = 5
        for _ in range(MAX_DIGITS):
            idx += str(randint(1, 6))   # simulate a dice
        #print('idx:', idx)
        res = self.words[idx]
        #print('res:', res)
        return res

    def request_words(self, n):
        ''' request words '''
        results = list()
        for _ in range(n):
            results.append(self.rand_words())
        res = ' '.join(results)
        res = res.strip()
        return res

def main():
    ''' main '''
    s = Solution()
    for _ in range(10):
        r = s.request_words(7)
        print(r)

if __name__ == '__main__':
    main()
