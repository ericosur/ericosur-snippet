#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
using sympy.factorint to factorize integers

it takes a while to load sympy (it's huge!)

melody's question, in a range of numbers, which number has most number of factors

for example, smaller than 1000, 840 has most factors (32)
'''

import sys

try:
    from sympy import factorint
except ImportError:
    print("need module sympy")
    sys.exit(1)

def get_num_factors(value: int) -> int:
    '''
    use sympy.factorint() and display in formatted form
    '''
    assert value >= 0

    # factorint() will return dict with factor and its
    myd = factorint(value)
    # output the result...
    #print(value, "= ", end='')
    t = 1
    for v in myd.values():
        #print(v)
        t *= (v + 1)
    return t

def main() -> None:
    '''main function'''
    lower = 4
    upper = 1_000
    max_k = 1
    max_v = 1
    for x in range(lower, upper):
        ret = get_num_factors(x)  # get the number of factors of x
        if ret > max_v:
            max_k = x
            max_v = ret
            print(f'{max_k} : {max_v}')


if __name__ == '__main__':
    main()
