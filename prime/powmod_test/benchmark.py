#!/usr/bin/env python3
# coding: utf-8

'''
benchmark of powmod implementation
'''

import os
import sys
from random import randint
#from math import ceil
import timeit

def powmod(b, e, m):
    ''' power modulus '''
    v = 1
    s = e
    while s > 0:
        v *= b
        v = v % m
        s -= 1
    return v    # the remainder


def main():
    ''' main '''
    p = './fast-modular-exponentiation/python/'
    if os.path.isdir(p):
        sys.path.insert(0, './fast-modular-exponentiation/python/')
        from main import fast_exp
    else:
        print('[WARN] need submodule fast-modular-exponentiation...')
        sys.exit(1)

    def milli(start, end):
        ''' get milli '''
        return round((start - end) * 1e6, 2)

    def myfmt(n: int) -> str:
        ''' my format '''
        s = '{:-10.2f}'.format(n)
        return s

    print('{:12s}{:12s}{:12s}'.format('   builtin', '   powmod', 'fast_exp'))
    print('-' * 40)
    time_takes = list()
    for _ in range(10):
        time_takes.clear()
        b = randint(999999, 9999999)
        e = randint(99999, 999999)
        m = randint(9999, 999999)

        t0 = timeit.default_timer()
        a = pow(b, e, m)    # python built-in
        time_takes.append(milli(timeit.default_timer(), t0))

        t0 = timeit.default_timer()
        r1 = powmod(b, e, m)
        assert a == r1
        time_takes.append(milli(timeit.default_timer(), t0))

        t0 = timeit.default_timer()
        r2 = fast_exp(b, e, m)
        assert a == r2
        time_takes.append(milli(timeit.default_timer(), t0))

        print(' '.join(map(myfmt, time_takes)))
        #print('builtin vs powmod vs fast_exp:', time_takes)

if __name__ == '__main__':
    main()
