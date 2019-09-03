#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" want to know if randint is uniform """

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
    print('max: {:3f}, min: {:.3f}, '.format(max(arr), min(arr)), end='')
    print('stddev: {:.3f}'.format(s))


def main():
    """ main function to do test """
    for _ in range(10):
        ar = test()
        show(ar)


if __name__ == '__main__':
    main()
