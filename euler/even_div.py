#!/usr/bin/env python3
# code: utf-8

'''
even divide
'''

import numpy as np

def test_even_divide(nn):
    ''' test even divide '''
    block = []
    for i in range(1, 20):
        if nn % i != 0:
            block.append(i)

    return len(block)==0, block

def test_number(nn):
    ''' main '''
    res, block = test_even_divide(nn)
    if res:
        print(f"{nn} can be evenly divided")
    else:
        print(f'{nn} cannot be evenly divided due to: {block}')


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
