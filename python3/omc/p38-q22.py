#!/usr/bin/env python3
# coding: utf-8

'''
P38. Q22
x = 1/2 x 3/4 x 5/6 x ... x 47/48
y = 2/3 x 4/5 x 6/7 x ... x 48/49
z = 1/7

'''

from sympy import Rational

def get_product(xn, xd):
    ''' return product '''
    seven = Rational(1,7)
    b = 0
    xpairs = zip(xn, xd)
    prod = 1
    for x in xpairs:
        (m, n) = x
        r = Rational(m, n)
        prod *= r
        if prod > seven:
            print('.', end='')
            b += 1
    print(b)
    return prod



def main():
    ''' main '''
    print(__doc__)
    xn = list(range(1,49,2))
    xd = list(range(2,49,2))
    x = get_product(xn, xd)
    print(f'got {x=}', float(x))
    yn = list(range(2,50,2))
    yd = list(range(3,50,2))
    y = get_product(yn, yd)
    print(f'got {y=}', float(y))

    z = Rational(1,7)
    print(f'{x} - {z} = {x-z}')
    print(f'{y} - {z} = {y-z}')
    print(f'{x} - {y} = {x-y}')


if __name__ == '__main__':
    main()
