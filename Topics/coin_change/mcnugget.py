#!/usr/bin/env python3

'''
try to find McNugget Number
https://mathworld.wolfram.com/McNuggetNumber.html
'''

import itertools as it
import operator
import bisect
from math import ceil

def check_missing(res: list, maxnum: int) -> list:
    '''
    return missing number in list
    '''
    missing = []
    for ii in range(1, maxnum+1):
        if not ii in res:
            missing.append(ii)
    return missing


def main():
    ''' main test function '''

    # if 4 elem for McNugget
    # m = (4, 6, 9, 20)

    m = (6, 9, 20)
    MAXNUMBER = 100

    pp = list(range(ceil(MAXNUMBER/m[0])))
    qq = list(range(ceil(MAXNUMBER/m[1])))
    rr = list(range(ceil(MAXNUMBER/m[2])))

    # if 4 elem for McNugget
    # ss = list(range(ceil(MAXNUMBER/m[3])))

    res = []

    # using itertools without writing more nested for-loop
    # if 4 elem for McNugget, add __ss__ into next tuple
    for n in it.product(pp, qq, rr):
        # m dot product n
        ans = sum(map(operator.mul, m, n))
        if ans > MAXNUMBER:
            continue

        # ans > 0 and ans is not duplicated
        if ans and not ans in res:
            bisect.insort(res, ans)
            #print('n: {} ans: {}'.format(n, ans))

    print('res: {}'.format(res))
    missing = check_missing(res, MAXNUMBER)
    #print('missing: {}'.format(missing))
    print('McNugget Number: {}'.format(missing[-1]))

if __name__ == '__main__':
    main()
