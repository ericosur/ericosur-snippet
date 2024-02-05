#!/usr/bin/env python3
# coding: utf-8

'''
similar to coin change problem
three type of coin, 411, 295, 161
and 8, 11, 20 respectively

what is the combination to target?
'''

import itertools as it
import operator
import sys
from typing import List

import numpy as np


class Solution():
    ''' solution for coin change problem '''
    def __init__(self, coins: List, limits: List, target: int):
        self.coins = coins
        self.limits = limits
        self.target = target
        self.candidates = []
        self.valid = self.check_max()

    def check_max(self) -> bool:
        ''' check max '''
        max_value = np.dot(self.coins, self.limits)
        if self.target > max_value or self.target < 0:
            print(f'impossible REACH the target({self.target}), max({max_value})')
            return False
        return True

    def list_all_candidate(self):
        ''' list all candidate '''
        ii = list(range(self.limits[0]))
        jj = list(range(self.limits[1]))
        kk = list(range(self.limits[2]))
        self.candidates = list(it.product(ii, jj, kk))

    def solve(self):
        ''' solve '''
        if not self.valid:
            print('[FAIL] impossible to solve')
            sys.exit(1)

        MAX_FOR_PRINT = 30
        answers = []
        self.list_all_candidate()
        for aa in self.candidates:
            # may use numpy.dot(coins, aa) if available
            t = sum(map(operator.mul, self.coins, aa))
            if t == self.target:
                answers.append(aa)
        if answers:
            print(f'number of possible answers: {len(answers)}')
            for ii, val in enumerate(answers):
                if ii >= MAX_FOR_PRINT:
                    print('......')
                    break
                print(val)
        else:
            print('no answers at all')

    # replaced by: sum(map(operator.mul, aa, bb))
    # @staticmethod
    # def dot_product(coins, ans):
    #     ''' stupid way to do dot product '''
    #     val = 0
    #     for ii, cc in enumerate(coins):
    #         val = val + cc * ans[ii]
    #     return val

    # replaced by: it.product(ii, jj, kk)
    # @staticmethod
    # def make_arr(all_limits, all_ans):
    #     ''' compose array '''
    #     for k in range(0, all_limits[2]):
    #         for j in range(0, all_limits[1]):
    #             for i in range(0, all_limits[0]):
    #                 one_val = [i, j, k]
    #                 all_ans.append(one_val)
    #     print('len(all_ans): ', len(all_ans))


def main():
    ''' main '''

    # # original problem
    # coins = [411, 295, 161]
    # limits = [8, 11, 20]
    # target = 3200

    coins = [411, 295, 161]
    limits = [8, 11, 20]
    target = 3200
    print(f'target: {target}')
    print(f'coins: {coins}')
    print(f'limits: {limits}')
    s = Solution(coins, limits, target)
    s.solve()


if __name__ == '__main__':
    main()
