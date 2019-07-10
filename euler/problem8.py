#!/usr/bin/env python3
# coding: utf-8

'''
problem 8
https://projecteuler.net/problem=8
'''

import bisect
import numpy as np

class SolveProblem8():
    ''' class to solve problem #8 '''
    def __init__(self):
        self.quest = None
        self.result = {}
        self.load()

    def __str__(self):
        ret = 'length = {}'.format(len(self.quest))
        return ret

    def load(self):
        ''' load '''
        with open('data8.txt', 'rt') as fh:
            raw_str = fh.read()
            self.quest = [int(ii) for ii in list(raw_str.strip().replace('\n', ''))]

    def test(self):
        ''' test '''
        test_len = 13
        x = []
        count = 0
        for ii in range(len(self.quest)-13+1):
            x = self.quest[ii:ii+test_len]
            if 0 in x:
                continue
            else:
                count += 1
                p = np.prod(x)
                if not p in self.result:
                    self.result[p] = x

        print('non-zero count', count)
        keys = list(self.result.keys())
        keys.sort()
        for ii in range(15):
            kk = keys[len(keys) - ii - 1]
            print("#{:02d} {:12d}: {}".format(ii, kk, self.result[kk]))


def main():
    ''' main '''
    sol = SolveProblem8()
    print(sol)
    sol.test()


if __name__ == '__main__':
    main()
