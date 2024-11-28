#!/usr/bin/env python3
# coding:utf-8

'''
three number cards
sum = 21
different numbers
'''

import itertools as it


class Solution():
    ''' solution '''
    def __init__(self):
        self.target = 21
        self.minimum = 1
        self.maximum = 19

    @staticmethod
    def is_different(a, b, c):
        ''' is different '''
        if a == b or b == c or c == a:
            return False
        return True

    @staticmethod
    def is_small2big(a, b, c):
        ''' a, b, c small to big '''
        if c > b > a:   # c > b and b > a
            return True
        return False

    def is_sum_match(self, a, b, c):
        ''' is sum(a,b,c) == target '''
        total = a + b + c
        if total == self.target:
            return True
        return False

    def test(self):
        ''' test '''
        assert self.is_different(1, 1, 2) is False
        assert self.is_different(1, 2, 2) is False
        assert self.is_different(2, 1, 2) is False
        assert self.is_different(1, 2, 3)
        assert self.is_sum_match(7, 7, 7)
        assert self.is_sum_match(6, 7, 8)

    def run(self):
        ''' run '''
        pp = list(range(self.minimum, self.maximum+1))
        # qq = list(range(self.minimum, self.maximum+1))
        # rr = list(range(self.minimum, self.maximum+1))
        cnt = 0
        for n in it.combinations(pp, 3):
            (p, q, r) = n
            if self.is_different(p, q, r):
                if self.is_small2big(p, q, r):
                    cnt += 1
                    if self.is_sum_match(p, q, r):
                        print(p, q, r)
        print('cnt:', cnt)

def main():
    ''' main '''
    sol = Solution()
    sol.run()

if __name__ == '__main__':
    main()
