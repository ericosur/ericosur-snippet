#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' provide a recursive version of gcd '''

__version__ = '1.0.0'

from typing import List


def gcd(m: int, n: int) -> int:
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)

def lcm(m: int, n: int) -> int:
    ''' least common multiple '''
    return m // gcd(m, n) * n

def gcd_lcm(m: int, n: int) -> int:
    ''' return both gcd and lcm '''
    g = gcd(m, n)
    l = m // g * n
    return (g, l)

def gcd_list(values: List[int]):
    ''' input list of values and calculate gcd of them '''
    hh = values[0]
    for nn in values[1:]:
        g = gcd(hh, nn)
        hh = g
    print(hh)


def lcm_list(values: List[int]):
    ''' lcm of a list '''
    hh = values[0]
    for nn in values[1:]:
        ll = lcm(hh, nn)
        hh = ll
    print(hh)


def test():
    ''' test '''
    m = 1280
    n = 1024
    (g, l) = gcd_lcm(m, n)
    print(f'{m} {n}: {g}, {l}')

def test2():
    ''' test2 '''
    v = [2, 3, 7, 78, 91]
    gcd_list(v)
    lcm_list(v)

def main():
    ''' main '''
    test2()

if __name__ == '__main__':
    main()
