#!/usr/bin/python
# coding: utf-8

'''
problem:
1. 4 digits
2. new number is 4 times bigger than old one
3. it is reversed, eg 1234 -> 4321
'''

import itertools as it
import numpy as np

def valueOf(p):
    ''' get scalar value of list p '''
    b = [1000, 100, 10, 1]
    r = sum(np.multiply(b, p))
    return r

def test():
    ''' try the value to meet the problem '''
    d = list(range(1, 10))  # 1 .. 9
    for dd in it.product(d, d, d, d):
        pp = list(dd)
        qq = list(dd)
        qq.reverse()

        x = valueOf(pp)
        y = valueOf(qq)
        if y / 4 == x:
            print(x, y)

def main():
    ''' main '''
    print(__doc__)
    test()

if __name__ == '__main__':
    main()
