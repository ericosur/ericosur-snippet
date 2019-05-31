#!/usr/bin/env python3
# coding: utf-8
#

'''
using numpy to generate sample data from normal distribution, and
validate how many items fetch from array to get similar mu and sigma
'''

from __future__ import print_function
import numpy as np

# pylint: disable=useless-object-inheritance
class ValidateGuassian(object):
    ''' class ValidateGuassian '''
    def __init__(self):
        self.orig_arr = []
        self.target_mean = (100.0, 0.5)    # target mean, and limit
        self.target_stdev = (15.0, 0.75)   # target stdev, and limit
        self.result_mean = 0.0
        self.result_stdev = 0.0
        self.target_array_size = 10000
        self.fill_array()

    def fill_array(self):
        ''' fill array '''
        self.orig_arr = np.random.normal(self.target_mean, self.target_stdev,
                                         self.target_array_size)

    def validate_array(self, arr):
        '''
        given arr
        if mean and stdev of *arr* is close to target_mean and target_stdev,
        return true
        '''

        #print('there are {} elements'.format(len(arr)))
        mean = np.mean(arr)
        #median = np.median(arr)
        stdev = np.std(arr)
        #print('median: {:.3f}\n'.format(media))
        #print('mean: {:.3f}\nstdev: {:.3f}\n'.format(mean, stdev))
        if abs(self.target_mean[0] - mean) < self.target_mean[1] \
            and abs(self.target_stdev[0] - stdev) < self.target_stdev[1]:
            self.result_mean = mean
            self.result_stdev = stdev
            return True

        return False

    def test(self):
        ''' test '''
        np.random.shuffle(self.orig_arr)
        max_bound = len(self.orig_arr)
        step_bound = 50
        curr_bound = step_bound
        while curr_bound <= max_bound:
            if self.validate_array(self.orig_arr[:curr_bound]):
                break
            curr_bound += step_bound
        print('fetch {} elements and pass critria'.format(curr_bound))
        print('mean: {:.3f}\nstdev: {:.3f}'.format(self.result_mean, self.result_stdev))

def main():
    ''' main '''
    REPEAT = 10
    for _ in range(REPEAT):
        valid_guass = ValidateGuassian()
        valid_guass.test()


if __name__ == '__main__':
    main()
