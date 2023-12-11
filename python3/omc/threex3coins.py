#!/usr/bin/env python3
# coding: utf-8

'''
3 5-cent coins
3 1-dime coins
3 5-dime coins
'''

import itertools as it
import operator


class Solution():
    ''' solution '''
    coins = [3, 3, 3]
    values = [50, 10, 5]
    TOTAL = 100

    def __init__(self):
        self.answers = []

    def is_valid(self, p, q, r):
        ''' is valid for question '''
        if p < 1 or q < 1 or r < 1:
            return False
        if (p+q+r) <= self.TOTAL:
            return True
        return False

    def find_answer(self):
        ''' run this '''
        pp = list(range(1,4))
        qq = list(range(1,4))
        rr = list(range(1,4))
        cnt = 0
        for n in it.product(pp, qq, rr):
            cnt += 1
            ans = sum(map(operator.mul, self.values, n))

            if ans in self.answers:
                print(f'{n}, {ans} has in the answers')
            else:
                print(n, ans)
                self.answers.append(ans)

        print(f'{cnt=}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.find_answer()


def main():
    ''' main '''
    print('main')
    Solution.run()

if __name__ == '__main__':
    main()
