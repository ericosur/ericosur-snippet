#!/usr/bin/env python3

'''
compare traditional way vs numpy methods

if need to calculate massive large array, use numpy if possible
'''


import timeit

import numpy as np

DEFAULT_SIZE = 10000
DEFAULT_NUMBER = 10000

def fill_randit():
    ''' fill rand int with size '''
    return np.random.randint(100, size=DEFAULT_SIZE)

def fill_stupid() -> list[int]:
    ''' my own stupid way to fill array '''
    return list(range(DEFAULT_SIZE))

def sum_stupid(arr):
    ''' sum up '''
    s = 0
    for i in arr:
        s += i
    return s

def fill_inc():
    ''' fill array with increasing number '''
    return np.arange(0, DEFAULT_SIZE)

def test1():
    ''' test1 '''
    arr = fill_stupid()
    sum_stupid(arr)


def test2():
    ''' test2 '''
    arr = fill_inc()
    np.sum(arr)


def main():
    ''' main '''
    r0 = timeit.timeit("test1()", setup='from __main__ import test1', number=DEFAULT_NUMBER)
    r1 = timeit.timeit("test2()", setup='from __main__ import test2', number=DEFAULT_NUMBER)
    print(f'r0: {r0}\nr1: {r1}\n')

if __name__ == '__main__':
    main()
