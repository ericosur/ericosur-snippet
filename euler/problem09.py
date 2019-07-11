#!/usr/bin/env python3
# coding: utf-8

'''
http://projecteuler.net/problem=9
'''

from math import sqrt, ceil

def square_sum(m, n):
    ''' square and sum '''
    return m * m + n * n

def test_square(val):
    ''' test square '''
    root = sqrt(val)
    if root == ceil(root):
        return True
    return False

def main():
    ''' main '''
    cnt = 0
    sqcnt = 0
    for xx in range(1, 999):
        for yy in range(xx + 1, 999 - xx):
            cnt += 1
            sqsum = square_sum(xx, yy)
            sqroot = sqrt(sqsum)
            if sqroot < yy:
                break
            if test_square(sqsum):
                sqcnt += 1
                if xx + yy + sqroot == 1000:
                    print(xx, "^2 + ", yy, "^2 = ", sqroot, "^2")
    print("cnt = ", cnt)
    print("sqcnt = ", sqcnt)


if __name__ == '__main__':
    main()
