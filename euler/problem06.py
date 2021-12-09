#!/usr/bin/env python3
# coding: utf-8

'''
http://projecteuler.net/problem=6
'''

def sum_series(n):
    ''' sum up 1, 2, ..., n  and then squre '''
    s = (1 + n) * n // 2
    return s * s

def sqare_sum(n):
    '''
    sum of square numbers
    '''
    i = 1
    s = 0
    while i <= n:
        s += i*i
        i += 1
    return s

def pyramidal(n):
    '''
    [Square pyramidal number](https://en.wikipedia.org/wiki/Square_pyramidal_number)
    sum of 1^2, 2^2, 3^2, 4^2 ...
    '''
    r = pow(n, 3) / 3 + pow(n, 2) / 2 + (n / 6)
    return int(r)


def main():
    ''' main '''
    upper = 100
    mm = sum_series(upper)
    nn = sqare_sum(upper)
    dist = int(mm - nn)
    print(f'{mm}, {nn}, {dist}')
    print('r:', pyramidal(upper))

if __name__ == '__main__':
    main()
