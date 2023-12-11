#!/usr/bin/env python3
# coding: utf-8

'''
compare traditional way vs numpy methods

if need to calculate massive large array, use numpy if possible
'''

from __future__ import print_function

import timeit

import numpy as np

DEFAULT_SIZE = 10000
DEFAULT_NUMBER = 10000

def fill_randit():
    ''' fill rand int with size '''
    return np.random.randint(100, size=DEFAULT_SIZE)

def fill_stupid():
    ''' my own stupid way to fill array '''
    res = []
    for i in range(DEFAULT_SIZE):
        res.append(i)
    return res

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
