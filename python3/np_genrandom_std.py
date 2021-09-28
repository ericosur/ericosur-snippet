#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Generate random numbers that meets standard normal distribution

Functions using numpy:
rng, random, standard_normal, mean, median, std, amax, amin
'''

import time
import numpy as np

#pylint: disable=invalid-name

class GenerateStdNormal():
    ''' a class to generate standard normal '''

    default_size = 100000

    def __init__(self):
        self.mu = 55.5
        self.sigma = 7.87
        self.rng = np.random.default_rng(int(time.time()))   # np's random number generator

    def fill_bytes(self):
        ''' fill buffer '''
        arr = self.rng.integers(0, 256, self.default_size, dtype='uint8') # 0 .. 255
        return arr

    def fill_stdnorm(self):
        ''' fill buffer '''
        arr = self.mu + self.sigma * self.rng.standard_normal(size=self.default_size)
        return arr

    @staticmethod
    def show(arr: list):
        ''' show '''
        print(f'{np.amax(arr):.2f}, {np.amin(arr):.2f}, ', end='')
        print(f'{np.mean(arr):.2f}, {np.median(arr):.2f}, ', end='')
        print(f'{np.std(arr):.2f}, {len(arr)}')



    def test2(self):
        ''' use lambda, add 4 into all elements '''
        add2 = lambda x: x + 4
        for _ in range(10):
            r = add2(self.fill_stdnorm())
            self.show(r)

    def filter_arr(self, arr):
        ''' filter out beyond -n * sigma to n * sigma '''
        n = 3
        tmp = [ x for x in arr if x > self.mu - n*self.sigma ]
        r = [ x for x in tmp if x < self.mu + n*self.sigma ]
        return r

    @staticmethod
    def header():
        ''' print header '''
        print('  max,   min,  mean, median, stddev')

    def action(self):
        ''' flow '''
        n = 1.5
        self.header()
        for _ in range(10):
            r = self.fill_stdnorm()
            rb = self.filter_arr(r)
            llimit = r.mean()-n*r.std()
            rlimit = r.mean()+n*r.std()
            print(f"filter:{llimit:.2f}  {rlimit:.2f}")
            self.show(r)
            self.show(rb)
            print('-' * 40)

def main():
    """ main function to do test """
    q = GenerateStdNormal()
    q.action()

if __name__ == '__main__':
    main()
