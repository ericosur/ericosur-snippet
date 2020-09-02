#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
try to calculate p ** q mod n

it is used by last_digit_power.py
'''

import random

def _powmod(p, q, n):
    '''
        驗證答案是否正確
    '''
    return p ** q % n


def powmod(p, q, n):
    ''' power modulus '''
    v = 1
    s = q
    while s > 0:
        v *= p
        v = v % n
        s -= 1
    return v    # 得到的餘數


def test(rep):
    '''
    n: repeat time
    '''
    for _ in range(rep):
        (p, q, n) = (random.randint(10001, 99999),
                     random.randint(3001, 7999),
                     random.randint(1001, 3001))
        cc = _powmod(p, q, n)
        dd = powmod(p, q, n)
        print('{:6d} ** {:5d} % {:5d} = {}'.format(p, q, n, dd))

        assert dd == pow(p, q, n)
        assert dd == cc


if __name__ == '__main__':
    test(20)
