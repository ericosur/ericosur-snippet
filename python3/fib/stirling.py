#!/usr/bin/env python3
# coding: utf-8

'''
using Stirling's approx to get fib value

reference from:
http://zh.wikipedia.org/zh-tw/%E9%9A%8E%E4%B9%98

and Stirling's approximation
https://zh.wikipedia.org/wiki/%E6%96%AF%E7%89%B9%E9%9D%88%E5%85%AC%E5%BC%8F

'''

from math import exp, sqrt, pi
#from math import log
from calc_factorial import CalcFactorial

def est_fib(m):
    ''' implementation '''
    _lower = 1.0/(12.0*m+1.0)
    _upper = 1.0/(12.0*m)
    _avg = (_lower + _upper) / 2.0
    ans = sqrt(2.0*pi*m) * (m/exp(1.0))**m * exp(_avg)
    return ans

def main():
    ''' main function '''
    # the max number est_fib() could calculate
    n = 170

    with CalcFactorial() as cfact:
        real = cfact.factorial(n)
        ret = float(real)
        est = est_fib(n)
        print("{}! = {}".format(n, ret))
        print(" est = {}".format(est))
        print('abs = {}'.format(abs(ret-est)))

if __name__ == '__main__':
    main()
