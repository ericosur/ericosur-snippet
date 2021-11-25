#!/usr/bin/python3
# coding: utf-8

'''
NOTE: pythonista version

use StorePrime

'''

import os
import sys
import pickle
import re
import random

# pythonista
PYTHONISTA=False
DEBUG=False

if PYTHONISTA:
    import clipboard
    import console

from store_prime import StorePrime

__version__ = '2021.11.25.11.46'

# pylint: disable=invalid-name
def show(v, p, q):
    ''' show '''
    if p is None and q is None:
        return
    if q is None:
        s = f'{v} is a prime'
        if PYTHONISTA:
            console.alert(s)
        else:
            print(s)

    else:
        lhs = abs(v - p)
        rhs = abs(v - q)
        if lhs <= rhs:
            arrow = "<<<<<"
        else:
            arrow = ">>>>>"
        s = f'{v} is in the range of ({p} {arrow} {q})'
        if PYTHONISTA:
            console.alert(s)
        else:
            print(s)
def main():
    ''' main function '''
    with StorePrime() as sp:

        ''' inner function '''
        def test(v):
            ''' test '''
            (p, q) = sp.search_between_idx(v)
            if DEBUG: print(f'p:{p}, q:{q}')
            if p is None:
                print('\tno answer for this')
                return
            show(v, sp.at(p), sp.at(q))
            if PYTHONISTA:
                clipboard.set(str(sp.at(p)))


        if PYTHONISTA:
            ret = console.input_alert('input a number')
            try:
                val = int(ret)
                test(val)
            except ValueError:
                print(f'{ret} is a ValueError')
        else:
            for r in [101, 103, 202, 301, 307]:
                test(r)

if __name__ == '__main__':
    main()
