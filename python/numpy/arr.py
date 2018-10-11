#!/usr/bin/env python2
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

def test3():
    print('\nSome examples for using numpy:')
    print('min: {}, max: {}'.format(np.min(L), np.max(L)))
    print('std: {}, mean: {} avg: {}'.format(np.std(L), np.mean(L), np.average(L)))


def main():
    print('time taken with python sum():')
    print(timeit.timeit("test1()", setup='from __main__ import test1', number=100))
    print('time taken with numpy.sum()...')
    print(timeit.timeit("test2()", setup='from __main__ import test2', number=100))

    test3()


if __name__ == '__main__':
    main()
