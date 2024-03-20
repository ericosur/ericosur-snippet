#!/usr/bin/env python3
# coding: utf-8

'''
P25 Q3. 以下四個正整數中哪個是完全平方數？
921438, 2660161, 76186, 750235
'''

from math import sqrt
from utils import digit_root, digit_sum

def test(n):
    ''' test '''
    # if tail number is 1,4,5,6,9
    ps_tails = {1,4,5,6,9}
    remain = n % 10
    if not remain in ps_tails:
        print(f'the last digit of {n} does not in the {ps_tails}')
        return False

    ps_digitroot = {1,4,7,9}
    r = digit_root(n)
    s = digit_sum(n)
    print(f'{n}: {r}, {s}')
    return r in ps_digitroot

def main():
    ''' main '''
    values = [921438, 2660161, 76186, 750235]
    for v in values:
        if test(v):
            print(f'{v} is perfect square')


if __name__ == '__main__':
    main()
