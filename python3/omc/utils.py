#!/usr/bin/env python3
# coding: utf-8

'''
provides some common use functions
'''

from sympy import ntheory

MODULES="utils"
VERSION="2024.03.19"


def is_prime(n):
    ''' true if n is a prime number '''
    return ntheory.primetest.isprime(n)

def digit_sum(n):
    ''' given number n, return sum of digits
    n = 1234, return 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    return sum(ns)


def digit_root(n):
    '''
    should be < 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    rs = sum(ns)
    if rs < 10:
        return rs
    return digit_root(rs)


def A002113_list(nMax):
    '''
    return a list of palindrome numbers <= nMax
    OEIS A002113
    '''
    mlist=[]
    for n in range(nMax+1):
        mstr=str(n)
        if mstr==mstr[::-1]:
            mlist.append(n)
    return mlist

def to_ternary(n):
    """
    將十進位數轉換為三進位數
    """
    result = ""
    while n > 0:
        result = str(n % 3) + result
        n //= 3
    return result

def gcd(m: int, n: int) -> int:
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)
