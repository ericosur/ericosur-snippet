#!/usr/bin/env python3
# coding: utf-8

'''
inner product
'''

import numpy as np


class Solution():
    ''' solution '''

    names = [
        "0050", "0056", "006208", "00692", "00713",
        "00850", "00878", "00919", "00929", "2885",
        "2886", "2891", "4938", "5880"
    ]

    p10 = [
        121.15, 32.69, 70.1, 30.33, 46.02,
        32.13, 19.5, 20.19, 17.08, 24.3,
        36.7, 24.35, 75.4, 25.15]
    p11 = [
        131.35, 35.08, 74.95, 31.68, 49.58,
        34.05, 20.59, 21.65, 18.32, 26,
        39.5, 27.35, 81.2, 26.95]
    nums = [
        0, 30_000, 0, 0, 0,
        22_000, 55_000, 0, 0, 20_000,
        27_000, 12_000, 9_000, 35_000
    ]

    def __init__(self):
        self.sum10 = 0
        self.sum11 = 0

    def action(self):
        ''' action '''
        self.sum10 = np.dot(self.p10, self.nums)
        self.sum11 = np.dot(self.p11, self.nums)
        print(f'{self.sum10=}')
        print(f'{self.sum11=}')

        print('id, stock_size, price_diff, price_percent, value_diff, value_percent')
        total_diff = self.sum11 - self.sum10
        for i, n in enumerate(self.nums):
            if n <= 0:
                continue
            diff = self.p11[i] - self.p10[i]
            perc = diff / self.p10[i] * 100
            t = diff * self.nums[i]
            tp = t / total_diff * 100
            print(f'{self.names[i]:6s}, {self.nums[i]:6d}, ', end='')
            print(f'{diff:.2f}, {perc:4.2f}%, ${t:.0f}, {tp:.2f}%')


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
