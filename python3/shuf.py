#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
a simple demo to ultilize function in the other script
'''


import random
import timeit

import numpy as np
from fisher_yates_shuffle import shuffle_array

SIZE = 10000
DEFAULT_NUMBER = 5000
#ARR = [i for i in range(SIZE)]
ARR = list(range(SIZE))

def test1():
    ''' test1 '''
    shuffle_array(ARR)

def test2():
    ''' test2 '''
    random.shuffle(ARR)

def test3():
    ''' test3 '''
    np.random.shuffle(ARR)

def main():
    ''' demo multiple way to shuffle a numeric list '''
    print('start timeit...')
    tt = timeit.timeit("test3()", setup='from __main__ import test3', number=DEFAULT_NUMBER)
    print('  duration np.random.shuffle:', tt)
    tt = timeit.timeit("test2()", setup='from __main__ import test2', number=DEFAULT_NUMBER)
    print('  duration random.shuffle:', tt)
    tt = timeit.timeit("test1()", setup='from __main__ import test1', number=DEFAULT_NUMBER)
    print('  duration my shuffle_array:', tt)


if __name__ == '__main__':
    main()
