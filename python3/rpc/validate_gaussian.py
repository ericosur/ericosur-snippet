#!/usr/bin/env python3
# coding: utf-8
#

'''
get data from file and try to fetch part of them, to see
how many data will match the range of mu and sigma
'''

# pylint: disable=broad-except

from __future__ import print_function
import random
import statistics

# pylint: disable=useless-object-inheritance
class ValidateGuassian(object):
    ''' class ValidateGuassian '''
    def __init__(self):
        self.orig_arr = []
        self.target_mean = (100.0, 0.5)    # target mean, and limit
        self.target_stdev = (15.0, 0.75)   # target stdev, and limit
        self.result_mean = 0.0
        self.result_stdev = 0.0
        self.result_mode = 0.0
        self.orig_arr = self.read_array_from_file('data.txt')

    @staticmethod
    def read_array_from_file(fn):
        ''' read array from file '''
        arr = []
        try:
            with open(fn, 'rt') as ifile:
                for ln in ifile:
                    val = float(ln.strip())
                    arr.append(val)
        except IOError:
            print('IOError')
        return arr

    @staticmethod
    def save_array_to_file(arr, fn):
        ''' save array to file '''
        try:
            with open(fn, 'wt') as ofile:
                for val in arr:
                    print('{}'.format(val), file=ofile)
        except Exception as e:
            print('Except happens: {}'.format(e))

    @staticmethod
    def shuffle_array(arr):
        '''shuffle array using fisher'''
        n = len(arr)
        while n > 1:
            k = random.randint(0, n-1)
            n = n - 1
            arr[n], arr[k] = arr[k], arr[n]
        return arr


    def validate_array(self, arr):
        '''
        given arr
        if mean and stdev of *arr* is close to target_mean and target_stdev,
        return true
        '''

        #print('there are {} elements'.format(len(arr)))
        mean = statistics.mean(arr)
        #median = statistics.median(arr)
        stdev = statistics.stdev(arr)
        mode = 0
        # most time we could not get *mode* from this array, pass it
        try:
            mode = statistics.mode(arr)
        except statistics.StatisticsError:
            pass
        #print('median: {:.3f}\n'.format(media))
        #print('mean: {:.3f}\nstdev: {:.3f}\n'.format(mean, stdev))
        if abs(self.target_mean[0] - mean) < self.target_mean[1] \
            and abs(self.target_stdev[0] - stdev) < self.target_stdev[1]:
            self.result_mean = mean
            self.result_stdev = stdev
            self.result_mode = mode
            return True

        return False

    def test(self):
        ''' test data against critiria '''
        #test_arr = sorted(self.orig_arr)
        #self.save_array_to_file(test_arr, 'sorted.txt')

        test_arr = self.shuffle_array(self.orig_arr)
        max_bound = len(test_arr)
        step_bound = 50
        curr_bound = step_bound
        while curr_bound <= max_bound:
            if self.validate_array(test_arr[:curr_bound]):
                break
            curr_bound += step_bound
        print('fetch {} elements and pass critria'.format(curr_bound))
        print('mean: {:.3f}\nstdev: {:.3f}'.format(self.result_mean, self.result_stdev))
        if self.result_mode != 0:
            print('mode: {:.3f}'.format(self.result_mode))

def main():
    ''' main '''
    REPEAT = 10
    for _ in range(REPEAT):
        valguass = ValidateGuassian()
        valguass.test()

if __name__ == '__main__':
    main()
