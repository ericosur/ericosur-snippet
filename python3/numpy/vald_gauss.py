#!/usr/bin/env python3
# coding: utf-8
#

'''
using numpy to generate sample data from normal distribution, and
validate how many items fetch from array to get similar mu and sigma
'''

from __future__ import print_function

from random import randint

import numpy as np


class ValidateGuassian():
    ''' class ValidateGuassian '''
    def __init__(self):
        self.data_arr = []
        self.target_mean = (100.0, 0.5)    # target mean, and limit
        self.target_stdev = (15.0, 0.75)   # target stdev, and limit
        self.result_mean = 0.0
        self.result_stdev = 0.0
        self.target_array_size = randint(9999, 999999)
        self.fill_array()

    def fill_array(self):
        ''' fill array '''
        self.data_arr = np.random.normal(self.target_mean[0], self.target_stdev[0],
                                         self.target_array_size)

    def validate_array(self, arr):
        '''
        given arr
        if mean and stdev of *arr* is close to target_mean and target_stdev,
        return true
        '''
        #print(f'there are {len(arr)} elements'))
        mean = np.mean(arr)
        #median = np.median(arr)
        stdev = np.std(arr)
        #print(f'median: {media:.3f}\n')
        #print(f'mean: {mean:.3f}\nstdev: {stdev:.3f}\n')
        if abs(self.target_mean[0] - mean) < self.target_mean[1] \
            and abs(self.target_stdev[0] - stdev) < self.target_stdev[1]:
            self.result_mean = mean
            self.result_stdev = stdev
        else:
            print('NOT pass!')


    def printOut(self):
        ''' print out '''
        print(f'size: {self.target_array_size:7d}', end=' ')
        print(f'mean: {self.result_mean:8.3f}, stdev: {self.result_stdev:6.3f}', end=' ')
        print(f'({min(self.data_arr):.3f}, {max(self.data_arr):.3f})')


    def test(self):
        ''' test '''
        self.fill_array()
        self.validate_array(self.data_arr)
        self.printOut()


def main():
    ''' main '''
    REPEAT = 10
    for _ in range(REPEAT):
        valid_guass = ValidateGuassian()
        valid_guass.test()


if __name__ == '__main__':
    main()
