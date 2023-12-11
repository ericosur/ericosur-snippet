#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
fill array with random.randint, test it if uniform distributed
'''

import random
from statistics import stdev


def test(n=100000):
    ''' test '''
    upp = 10
    v = [0] * upp
    for _ in range(n):
        v[random.randint(0, upp-1)] += 1 # returns [0 .. 9]

    arr = []
    for _, x in enumerate(v):
        r = float(x) * 100.0 / float(n)
        arr.append(r)
        #print("{}: {:>6.3f}".format(i, r))
    return arr


def show(arr: list):
    ''' show '''
    s = stdev(arr)
    print(f'max: {max(arr):.3f}, min: {min(arr):.3f}, ', end='')
    print(f'stddev: {s:.3f}')


def main():
    """ main function to do test """
    for _ in range(10):
        ar = test()
        show(ar)


if __name__ == '__main__':
    main()
