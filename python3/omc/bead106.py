#!/usr/bin/env python3
# coding: utf-8

'''
3 persons get 106 beads
how many way to take
'''

import itertools as it


class Solution():
    ''' solution '''
    TOTAL = 106
    def __init__(self):
        self.ans = []

    def is_valid(self, p, q, r):
        ''' is valid for question '''
        if p < 1 or q < 1 or r < 1:
            return False
        if (p+q+r) <= self.TOTAL:
            return True
        return False

    def find_answer(self):
        ''' run this '''
        cnt = 0
        beads = range(1,self.TOTAL)
        for ii in it.combinations(beads, 3):
            (i,j,k) = ii
            if self.is_valid(i,j,k):
                self.ans.append(ii)
                print(ii)
                cnt += 1
        print(cnt)

    @classmethod
    def run(cls):
        ''' run this '''
        obj = cls()
        obj.find_answer()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
