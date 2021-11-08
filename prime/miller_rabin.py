#!/usr/bin/env python3
# coding: utf-8

'''
reference:
https://comeoncodeon.wordpress.com/2010/09/18/miller-rabin-primality-test/
'''

import random

def modulo(a, b, c):
    ''' modulo '''
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c
        y = (y * y) % c
        b = b // 2
    return x % c

def miller_rabin(n, iteration):
    ''' miller rabin '''
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d = d // 2
    for _ in range(iteration):
        a = random.randint(1, n - 1)
        temp = d
        #x = modulo(a, temp, n)
        x = pow(a, temp, n)     # use built-in function
        while temp != n - 1 and x != 1 and x != n - 1:
            x = (x * x) % n
            temp = temp * 2
        if x != n - 1 and temp % 2 == 0:
            return False
    return True


def test():
    ''' test '''
    for _ in range(10):
        (a, b, n) = (random.randint(201, 299), random.randint(101, 199), random.randint(11, 97))
        p = pow(a, b, n)
        q = modulo(a, b, n)
        assert p == q
        print(f'pow({a}, {b}, {n}) = {p}')
        #print("pow(%d, %d, %d) = %d" % (a, b, n, modulo(a, b, n)))


def main(n):
    ''' main '''
    print(n, 'is', (miller_rabin(n, 20) and "PRIME" or "COMPOSITE"))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('may specify numbers from cli...')
        main(795028841)
    else:
        if sys.argv[1] == 'test':
            test()
        else:
            for i in sys.argv[1:]:
                try:
                    main(int(i))
                except ValueError:
                    print(f'cannot convert "{i}" into integer')
