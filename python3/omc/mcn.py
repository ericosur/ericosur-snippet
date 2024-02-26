#!/usr/bin/env python3

'''
try to find McNugget Number
https://mathworld.wolfram.com/McNuggetNumber.html
'''

import itertools as it
from sympy import Rational

def checkVals(vals):
    ''' check validity of values '''
    target = Rational(11,10)
    s = 0
    for v in vals:
        t = Rational(1, v)
        s += t
    #print(vals, s)
    if target - s == 0:
        return True
    return False


def main():
    ''' main test function '''

    # if 4 elem for McNugget
    # m = (4, 6, 9, 20)

    UPPER = 19

    pp = list(range(1,UPPER))
    qq = list(range(1,UPPER))
    rr = list(range(1,UPPER))
    ss = list(range(1,UPPER))

    tries = []

    for n in it.product(pp, qq, rr, ss):
        if len(set(n)) == 4:
            if sum(list(n)) == 21:
                tries.append(list(n))

    print(f'size of tries: {len(tries)}')
    for t in tries:
        if checkVals(t):
            print(t)

if __name__ == '__main__':
    main()
