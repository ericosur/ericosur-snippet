#!/usr/bin/env python3
# code: utf-8

'''
even divide
'''

import numpy as np

def test_even_divide(nn):
    ''' test even divide '''
    for i in range(1, 20):
        if nn % i != 0:
            print('{} cannot divided by {}'.format(nn, i))
            return False
    return True

def test_number(nn):
    ''' main '''
    if test_even_divide(nn):
        res = 'can'
    else:
        res = 'cannot'
    print("{} {} be evenly divided".format(nn, res))


def gen_number():
    ''' gen a number '''
    items = [2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
    val = np.prod(items)
    return val

def main():
    ''' main '''
    test_number(232792560)
    test_number(939064810)

    gen = gen_number()
    test_number(gen)


if __name__ == '__main__':
    main()
