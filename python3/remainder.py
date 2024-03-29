#!/usr/bin/env python3
# coding: utf-8

'''
using brute force method to find a number X, which
mod 6 = 5
mod 7 = 6
mod 8 = 7

now I know the answer is the lcm(6, 7, 8) - 1

https://thispointer.com/python-check-if-all-values-are-same-in-a-numpy-array-both-1d-and-2d/
'''

import itertools as it

import numpy as np


class Solution():
    ''' class to solve the problem '''
    def __init__(self):
        self.arr = np.array((6, 7, 8))
        #self.A = np.array((2, 3, 4))

    def test1(self):
        ''' test1 '''
        r = np.lcm.reduce(self.arr)
        print('lcm:', r)

    def action(self):
        ''' action '''
        self.test1()
        C = self.arr - np.ones((1, 1))
        #print(C)
        #print(C.shape)
        p = list(range(1, 50))
        cnt = 0
        for x in it.product(p, p, p):
            cnt += 1
            r = self.arr * np.array(x) + C
            #print(f"x:{x} r:{r}")
            if np.max(r) == np.min(r):
                print(f"x:{x} r:{r}")
                print("all same")
                break
        print(f'{cnt} tried')

    @classmethod
    def run(cls):
        ''' run '''
        c = cls()
        c.action()


def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
