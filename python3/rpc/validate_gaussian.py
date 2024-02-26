#!/usr/bin/env python3
# coding: utf-8
#

'''
get data from file and try to fetch part of them, to see
how many data will match the range of mu and sigma
'''


from __future__ import print_function

import random
import statistics
import sys


class ValidateGuassian():
    ''' class ValidateGuassian '''
    def __init__(self):
        self.orig_arr = []
        self.target_mean = (100.0, 1.0)    # target mean, and limit
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
            with open(fn, 'rt', encoding='utf8') as ifile:
                for ln in ifile:
                    val = float(ln.strip())
                    arr.append(val)
        except IOError:
            print(f'[ERROR] IOError while open: {fn}')
            print('[INFO] may execute **req_guassian.py** to generate data.txt')
            sys.exit(1)
        return arr

    @staticmethod
    def save_array_to_file(arr, fn):
        ''' save array to file '''
        try:
            with open(fn, 'wt', encoding='utf8') as ofile:
                for val in arr:
                    print(f'{val}', file=ofile)
        except IOError as e:
            print(f'Except happens: {e}')

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

        if arr is None or len(arr) == 0:
            print('arr is None or zero size')
            raise ValueError

        #print('test size: {}', len(arr))
        mean = statistics.mean(arr)
        #median = statistics.median(arr)
        stdev = statistics.stdev(arr)
        mode = 0
        # most time we could not get *mode* from this array, pass it
        try:
            mode = statistics.mode(arr)
        except statistics.StatisticsError:
            #print('[WARN] statistics error:', e)
            pass

        def _show(n, low, high):
            ''' show '''
            print(f'{n:.3f} not in range ({low}, {high}) =====>')

        #print(f'median: {media:.3f}\n')
        #print(f'mean: {mean:.3f}\nstdev: {stdev:.3f}\n')
        self.result_mean = mean
        self.result_stdev = stdev
        self.result_mode = mode
        mean_pass = False
        stdev_pass = False
        if abs(self.target_mean[0] - mean) < self.target_mean[1]:
            mean_pass = True
        else:
            low = self.target_mean[0] - self.target_mean[1]
            high = self.target_mean[0] + self.target_mean[1]
            _show(mean, low, high)

        if abs(self.target_stdev[0] - stdev) < self.target_stdev[1]:
            stdev_pass = True
        else:
            low = self.target_stdev[0] - self.target_stdev[1]
            high = self.target_stdev[0] + self.target_stdev[1]
            _show(stdev, low, high)

        return (mean_pass, stdev_pass)

    def printOut(self):
        ''' print out '''
        print(f'mean: {self.result_mean:.3f}, stdev: {self.result_stdev:.3f}', end='')
        if self.result_mode != 0:
            print(f', mode: {self.result_mode:.3f}')
        else:
            print()


    def test(self):
        ''' test data against critiria '''
        #test_arr = sorted(self.orig_arr)
        #self.save_array_to_file(test_arr, 'sorted.txt')

        shuffled_arr = self.shuffle_array(self.orig_arr)
        max_bound = len(shuffled_arr)
        step_bound = random.randint(25, max_bound // 4)
        curr_bound = step_bound

        while True:
            test_arr = shuffled_arr[:curr_bound]
            m, n = self.validate_array(test_arr)
            print('test size:', len(test_arr), end=' ')
            if m and n:
                print('pass')
            else:
                if not m:
                    print('mean not pass: ', end='')
                if not n:
                    print('stdev not pass: ', end='')
                self.printOut()

            if curr_bound < max_bound:
                curr_bound += step_bound
            else:
                #print('out-of-range...')
                break


def main():
    ''' main '''
    REPEAT = 10
    for _ in range(REPEAT):
        valguass = ValidateGuassian()
        valguass.test()
        print('-' * 40)

if __name__ == '__main__':
    main()
