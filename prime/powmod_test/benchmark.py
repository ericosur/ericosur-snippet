#!/usr/bin/env python3
# coding: utf-8

'''
benchmark of powmod implementation
'''

#import os
import sys
#from math import ceil
import timeit
from random import randint
from statistics import mean, stdev


def powmod(b, e, m):
    ''' power modulus '''
    v = 1
    s = e
    while s > 0:
        v *= b
        v = v % m
        s -= 1
    return v    # the remainder

def show_stat(arr: list, msg: str):
    ''' show stat '''
    s = stdev(arr)
    m = mean(arr)
    print(f'{msg}: stdev:{milli(s):-12.0f}, mean:{milli(m):-12.0f}')

def milli(n):
    ''' get milli '''
    return round(n * 1e8, 0)

def main():
    ''' main '''
    p = './fast-modular-exponentiation/python/'
    try:
        sys.path.insert(0, p)
        # pylint: disable=import-outside-toplevel
        from main import fast_exp
    except ImportError:
        print('[WARN] need submodule: fast-modular-exponentiation...')
        sys.exit(1)


    # def myfmt(n: int) -> str:
    #     ''' my format '''
    #     s = f'{n:-10.2f}'
    #     return s

    builtin_time = []
    powmod_time = []
    fastexp_time = []

    for _ in range(100):
        b = randint(9999, 99999)
        e = randint(999999, 9999999)
        m = randint(9999, 99999)

        t0 = timeit.default_timer()
        a = pow(b, e, m)    # python built-in
        builtin_time.append(timeit.default_timer() - t0)

        t0 = timeit.default_timer()
        r1 = powmod(b, e, m)
        assert a == r1
        powmod_time.append(timeit.default_timer() - t0)

        t0 = timeit.default_timer()
        r2 = fast_exp(b, e, m)
        assert a == r2
        fastexp_time.append(timeit.default_timer() - t0)

        #print(' '.join(map(myfmt, time_takes)))
        #print('builtin vs powmod vs fast_exp:', time_takes)

    show_stat(builtin_time, "builtin")
    show_stat(powmod_time, " powmod")
    show_stat(fastexp_time, "fastexp")

if __name__ == '__main__':
    main()
