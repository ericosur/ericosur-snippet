#!/usr/bin/env python3
# coding: utf-8

'''
timeit on sum/npsum
'''

from __future__ import print_function

import timeit

import numpy as np


class TestSum():
    ''' class TestSum '''
    def __init__(self):
        self.data_arr = []
        self.data_size = 10000
        self.test_number = 8000
        self.fill_arr()

    def fill_arr(self):
        ''' fill array '''
        # integer value 0 to 99
        self.data_arr = np.random.randint(100, size=self.data_size)

    @staticmethod
    def print_duration(start, end, msg=''):
        ''' print duration '''
        between = end - start
        print(f'{msg} duration: {between:.3f} seconds (wall clock)')

    def test_sum(self):
        ''' test_sum '''
        time_start = timeit.default_timer()
        for _ in range(self.test_number):
            sum(self.data_arr)
        time_end = timeit.default_timer()
        TestSum.print_duration(time_start, time_end, 'test_sum')

    def test_npsum(self):
        ''' test_npsum '''
        time_start = timeit.default_timer()
        for _ in range(self.test_number):
            np.sum(self.data_arr)
        time_end = timeit.default_timer()
        TestSum.print_duration(time_start, time_end, 'test_npsum')

    def test(self):
        ''' test '''
        self.test_sum()
        self.test_npsum()


def main():
    ''' main '''
    tsum = TestSum()
    tsum.test()

if __name__ == '__main__':
    main()
