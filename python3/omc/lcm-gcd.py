#!/usr/bin/env python3
# coding: utf-8

'''
define an operation that A # B = lcm(A,B) - gcd(A,B)
find the max 24 # X, X is between 1, 100
'''

from math import gcd, lcm

#def lcm(m: int, n: int) -> int:
#    ''' get lcm '''
#    return (m*n) // gcd(m, n)

def ans(m, n):
    ''' get ans '''
    return lcm(m,n)-gcd(m,n)

def main():
    ''' main '''
    mpair = [0, 0]
    for x in range(1,101):
        r = ans(24, x)
        print(f'{x}: {r}')
        if r > mpair[1]:
            mpair = [x, r]
    print(mpair)

if __name__ == '__main__':
    main()
