#!/usr/bin/env python3
# coding: utf-8

'''
compare traditional way vs numpy methods

if need to calculate massive large array, use numpy if possible
'''

import numpy as np
import timeit

DEFAULT_SIZE = 10000
DEFAULT_NUMBER = 10000

def fill_randit():
    return np.random.randint(100, size=DEFAULT_SIZE)

def fill_stupid():
    res = []
    for i in range(DEFAULT_SIZE):
        res.append(i)
    return res

def sum_stupid(arr):
    s = 0
    for i in arr:
        s += i
    return s

def fill_inc():
    return np.arange(0, DEFAULT_SIZE)

def test1():
    arr = fill_stupid()
    s = sum_stupid(arr)
    #print('sum:', s)

def test2():
    arr = fill_inc()
    s = np.sum(arr)
    #print('sum:', s)

def main():
    r0 = timeit.timeit("test1()", setup='from __main__ import test1', number=DEFAULT_NUMBER)
    r1 = timeit.timeit("test2()", setup='from __main__ import test2', number=DEFAULT_NUMBER)
    print('r0: {}\nr1: {}\n'.format(r0, r1))

if __name__ == '__main__':
    main()
