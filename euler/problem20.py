#!/usr/bin/env python3
# coding: utf-8

'''
http://projecteuler.net/problem=20
'''

import numpy as np

def stupid_factorial(m):
    ''' studpid factorial '''
    if m <= 1:
        return 1
    return m * stupid_factorial(m - 1)

def main():
    ''' main '''
    result = stupid_factorial(100)
    print(result)
    allchar = list(str(result))
    allints = list(map(int, allchar[:]))
    print("sum:", np.sum(allints))

if __name__ == '__main__':
    main()
