#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" want to know if randint is uniform """

from __future__ import print_function
import random

def main():
    """ main function to do test """
    n = 100000
    upp = 10
    v = [0]*upp
    for i in xrange(n):
        v[random.randint(0, upp-1)] += 1 # returns [0 .. 9]

    i = 0
    for x in v:
        print("%d: %.4g" % (i, float(x)*100.0/float(n)))
        i += 1


if __name__ == '__main__':
    main()
