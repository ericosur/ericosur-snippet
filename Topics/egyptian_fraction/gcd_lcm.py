#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' provide a recursive version of gcd '''

__version__ = '1.0.0'

def gcd(m, n):
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)

def lcm(m, n):
    ''' least common multiple '''
    return m // gcd(m, n) * n

def gcd_lcm(m, n):
    ''' return both gcd and lcm '''
    g = gcd(m, n)
    l = m // g * n
    return (g, l)

def main():
    ''' main '''
    m = 1280
    n = 1024
    (g, l) = gcd_lcm(m, n)
    print('{} {}: {}, {}'.format(m, n, g, l))

if __name__ == '__main__':
    main()
