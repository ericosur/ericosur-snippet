#!/usr/bin/env python
'''
reference from http://www.cg45.cn/archives/246
to find P, which satisfy:
    P = m ** 2 + n ** 2
    P is a prime and P < 10000
    m and n are primes as well
'''

from math import sqrt
from MillerRabin import miller_rabin

def is_prime(nn):
    '''
        a wrapper function of miller_rabin()
    '''

    return miller_rabin(nn)

def test():
    '''
        m, n, P are primes,
        only n = 2 would make P odd because m and m*m are odd
    '''
    L = 3
    U = int(sqrt(99999))
    cnt = 0
    for m in range(L, U, 2):
        if is_prime(m):
            p = m**2 + 4
            if is_prime(p):
                print(f'{p} = {m}^2 + 2^2')
                cnt += 1
    return cnt

def main():
    ''' main '''
    result = test()
    print(f'get {result} results')


if __name__ == '__main__':
    main()
