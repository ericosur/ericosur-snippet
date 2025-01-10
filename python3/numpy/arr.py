#!/usr/bin/env python3
# coding: utf-8

''' numpy array sample '''

from __future__ import print_function
import sys
import timeit
import numpy as np
sys.path.insert(0, "..")
sys.path.insert(0, "python3")
from myutil import prt  # type: ignore[import]

class Solution():
    ''' solution '''
    MAXCNT = 1_000_000

    def __init__(self):
        self.vals = np.random.random(self.MAXCNT)

    def test1(self):
        ''' test1 '''
        sum(self.vals)

    def test2(self):
        ''' test2 '''
        np.sum(self.vals)

    @staticmethod
    def get_statistics(arr):
        ''' get statistics '''
        prt(f'min: {np.min(arr):.6f}, max: {np.max(arr):.6f}')
        prt(f'std: {np.std(arr):.6f}, mean: {np.mean(arr):.6f} avg: {np.average(arr):.6f}')

    # pylint: disable=unnecessary-lambda
    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        prt(f'Note: an np.narray with size ({obj.MAXCNT}), and repeat sum up')
        prt('normal python sum() will take lots of CPU time')
        REPEAT = 100
        #t =timeit.timeit("test1()", setup='from __main__ import test1', number=100)
        t = timeit.timeit(lambda: obj.test1(), number=REPEAT)
        prt(f'time taken with python sum(): {t:.6f}')
        t = timeit.timeit(lambda: obj.test2(), number=REPEAT)
        prt(f'time taken with numpy.sum():  {t:.6f}')

def main():
    ''' main '''
    #test()
    Solution.run()

if __name__ == '__main__':
    main()
