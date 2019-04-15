#!/usr/bin/env python

'''
try to find McNugget Number
http://mathworld.wolfram.com/McNuggetNumber.html

'''

from itertools import product
import operator
import bisect
from math import ceil

def check_missing(res, maxnum):
    missing = []
    for ii in range(1, maxnum+1):
        if not ii in res:
            missing.append(ii)
    return missing


def main():
    m = (6, 9, 20)
    MAXNUMBER = 100

    res = []
    for xx in range(ceil(MAXNUMBER/m[0])):
        for yy in range(ceil(MAXNUMBER/m[1])):
            for zz in range(ceil(MAXNUMBER/m[2])):
                n = (xx, yy, zz)

                # m dot product n
                ans = sum(map(operator.mul, m, n))
                if ans > MAXNUMBER:
                    continue

                # ans > 0 and ans is not duplicated
                if ans and not ans in res:
                    bisect.insort(res, ans)
                    print('n: {} ans: {}'.format(n, ans))

    print('res: {}'.format(res))
    missing = check_missing(res, MAXNUMBER)
    #print('missing: {}'.format(missing))
    print('McNugget Number: {}'.format(missing[-1]))

if __name__ == '__main__':
    main()
