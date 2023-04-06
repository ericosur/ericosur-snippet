#!/usr/bin/python3
# coding: utf-8

'''
3 persons get 106 beads
how many way to take
'''

import itertools as it

class Solution():
    TOTAL = 106
    def __init__(self):
        self.ans = []

    def is_valid(self, p, q, r):
        if p < 1 or q < 1 or r < 1:
            return False
        if (p+q+r) <= self. TOTAL:
            return True
        return False

    def find_answer(self):
        cnt = 0
        beads = range(1,self.TOTAL)
        for ii in it.combinations(beads, 3):
            (i,j,k) = ii
            if self.is_valid(i,j,k):
                self.ans.append(ii)
                print(ii)
                cnt += 1
        print(cnt)


def main():
    ''' main '''
    print('main')
    sol = Solution()
    sol.find_answer()

if __name__ == '__main__':
    main()
