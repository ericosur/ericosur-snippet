#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
using sympy.factorint to factorize integers

it takes a while to load sympy (it's huge!)
'''

import sys
from random import randint

from sympy import factorint


def show(value):
    '''
    use sympy.factorint() and display in formatted form
    '''
    assert value >= 0

    # factorint() will return dict with factor and its
    myd = factorint(value)
    # output the result...
    print(value, "= ", end='')
    arr = list(myd.keys())
    arr.sort()
    isFirst = True
    for key in arr:
        if not isFirst:
            print(" * ", end='')
        else:
            isFirst = False
        val = myd[key]
        if val == 1:
            print(key, end='')
        else:
            print(f"{key}**{myd[key]}", end='')


def main(argv: list):
    '''main function'''
    if argv == []:
        print("usage: factoring.py [arg1] [arg2]...")
        print()
        for _ in range(3):
            argv.append(randint(1001, 9999))

    for x in argv:
        try:
            value = int(x)
            show(value)
            print()
        except ValueError:
            print("not a numeric value:", x)
            continue
        # except:
        #     print("unexpected error:", sys.exc_info()[0])
        #     continue

if __name__ == '__main__':
    main(sys.argv[1:])
