#!/usr/bin/python3
# coding: utf-8

'''
https://en.wikipedia.org/wiki/Special_right_triangle

Pythagorean triple

'''

import math
import itertools as it
from gcd import gcd

def sqrt_sum(a, b):
    ''' sum '''
    return math.sqrt(a*a + b*b)

def test():
    ''' test '''
    max_side = 256
    a1 = []
    for (m, n) in it.combinations(range(1, max_side), 2):
        r = sqrt_sum(m, n)
        if math.floor(r) == math.ceil(r):
            #print('{}, {}: {}'.format(m, n, int(r)))
            g = gcd(m, n)
            if g == 1:
                a1.append((m, n, int(r)))
    print(a1)
    print(len(a1))


def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
