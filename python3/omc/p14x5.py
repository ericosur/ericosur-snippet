#!/usr/bin/python3
# coding: utf-8

'''
from (1,40) pick a,b (a<b and a!=b)
sum of a and b is 4m
'''

import itertools as it


def get_result(x):
    a = abs(x[0] - x[1])
    b = abs(x[1] - x[2])
    c = abs(x[2] - x[3])
    d = abs(x[3] - x[4])
    e = abs(x[4] - x[1])
    return a+b+c+d+e

def main():
    ''' main '''
    UPPER_LIMIT = 5

    v = list(range(1, UPPER_LIMIT+1))
    p = it.permutations(v, 5)
    wtf = []
    sums = []
    for x in p:
        ret = get_result(x)
        sums.append(ret)
        wtf.append((x, ret))

    sums.sort()
    print(sums)
    for i in wtf:
        print(i)


if __name__ == '__main__':
    main()
