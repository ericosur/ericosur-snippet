#!/usr/bin/env python3
# coding: utf-8

'''
求這樣的四位數，它等於它的各位數字之和的四次方
'''

def digit_sum(n):
    ''' given number n, return sum of digits
    n = 1234, return 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    return sum(ns)

def test(n):
    ''' test '''
    r = digit_sum(n)
    if pow(r, 4)==n:
        print(f'{n}: {r}')

def main():
    ''' main '''
    for i in range(1000,9999+1):
        test(i)

if __name__ == '__main__':
    main()
