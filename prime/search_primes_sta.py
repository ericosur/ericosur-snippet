#!/usr/bin/python3
# coding: utf-8

'''
NOTE: pythonista version

use StorePrime

'''

import sys
from store_prime import StorePrime

__version__ = '2023.04.10.11.02'

# pythonista
if sys.platform == 'linux':
    PYTHONISTA=False
else:
    PYTHONISTA=True

DEBUG=False

# pylint: disable=import-error
# pylint: disable=unused-import
if PYTHONISTA:
    import clipboard
    import console


# pylint: disable=invalid-name
def show(v, p, q):
    ''' show '''
    if p is None and q is None:
        return
    if q is None:
        s = f'{v} is a prime'
        if PYTHONISTA:
            console.alert('result', s, 'OK', hide_cancel_button=True)
        else:
            print(s)

    else:
        lhs = abs(v - p)
        rhs = abs(v - q)
        if lhs < rhs:
            arrow = "<-----"
        elif lhs == rhs:
            arrow = "<---->"
        else:
            arrow = "----->"
        s = f'{v} is in the range of ({p} {arrow} {q})'
        if PYTHONISTA:
            console.alert('result', s, 'OK', hide_cancel_button=True)
        else:
            print(s)

def main():
    ''' main function '''
    with StorePrime("small.txt", "small.p") as sp:
        # inner function
        def test(v):
            ''' test '''
            (p, q) = sp.search_between_idx(v)
            if DEBUG:
                print(f'p:{p}, q:{q}')
            if p is None:
                print('\tno answer for this')
                return
            show(v, sp.at(p), sp.at(q))
            if PYTHONISTA:
                clipboard.set(str(sp.at(p)))

        if PYTHONISTA:
            while True:
                ret = console.input_alert('input a number')
                try:
                    val = int(ret)
                    if val <= 0:
                        break
                    test(val)
                except ValueError:
                    msg = f'ValueError: {ret}'
                    console.alert(msg)  # will break while-loop
        else:
            for r in [101, 103, 202, 301, 307]:
                test(r)

if __name__ == '__main__':
    main()
