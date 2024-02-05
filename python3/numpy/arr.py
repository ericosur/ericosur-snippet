#!/usr/bin/env python3
# coding: utf-8

''' numpy array sample '''

from __future__ import print_function

import timeit

import numpy as np


MAXCNT = 75000
L = np.random.random(MAXCNT)

def test1():
    ''' test1 '''
    sum(L)
    #print('result:', S1)

def test2():
    ''' test2 '''
    np.sum(L)
    #print('result:', S2)

def get_statistics(arr):
    ''' get statistics '''
    print(f'min: {np.min(arr)}, max: {np.max(arr)}')
    print(f'std: {np.std(arr)}, mean: {np.mean(arr)} avg: {np.average(arr)}')

def test():
    ''' test '''
    arr = L
    print('array filled with 0 to 1')
    get_statistics(arr)
    mu, sigma = 0.5, 0.25
    print(f'array filled with normal distribution mu:{mu} sigma:{sigma}')
    arr = np.random.normal(mu, sigma, MAXCNT)
    get_statistics(arr)

def main():
    ''' main '''
    test()

    print('time taken with python sum():')
    print(timeit.timeit("test1()", setup='from __main__ import test1', number=100))
    print('time taken with numpy.sum()...')
    print(timeit.timeit("test2()", setup='from __main__ import test2', number=100))



if __name__ == '__main__':
    main()
