#!/usr/bin/env python3
#

''' numpy array sample '''

import numpy as np
import timeit

MAXCNT = 75000
L = np.random.random(MAXCNT)

def test1():
    S1 = sum(L)
    #print('result:', S1)

def test2():
    S2 = np.sum(L)
    #print('result:', S2)

def get_statics(arr):
    print('min: {}, max: {}'.format(np.min(arr), np.max(arr)))
    print('std: {}, mean: {} avg: {}'.format(np.std(arr), np.mean(arr), np.average(arr)))

def test():
    arr = L
    print('array filled with 0 to 1')
    get_statics(arr)
    mu, sigma = 0.5, 0.25
    print('array filled with normal distribution mu:{} sigma:{}'.format(mu, sigma))
    arr = np.random.normal(mu, sigma, MAXCNT)
    get_statics(arr)

def main():
    test()

    print('time taken with python sum():')
    print(timeit.timeit("test1()", setup='from __main__ import test1', number=100))
    print('time taken with numpy.sum()...')
    print(timeit.timeit("test2()", setup='from __main__ import test2', number=100))



if __name__ == '__main__':
    main()
