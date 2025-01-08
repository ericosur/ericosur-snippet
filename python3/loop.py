#!/usr/bin/env python3
# coding: utf-8
#

'''
LOOP

use a quick/rough way to estimate how many years you need
if wannt to go double insterest

year \\approx 72 / insterest

for example, i = 5% one year iteration
72/5 = 14.4
about 14 year we could double the base
'''

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

def tryloop(r: float, _limit=2.0):
    ''' tryloop '''
    assert r > 0.0
    assert r < 1.0
    v = 1.0 + r
    ii = 0
    while v < _limit:
        ii += 1
        v *= 1 + r
    prt(f'tryloop: for r={r*100:.2f}%, need {ii} years to exceed {_limit}')

def loop2(r: float, _limit: float=2.0):
    ''' loop2 '''
    assert r > 0.0
    assert r < 1.0

    v = 1.0 + r
    base = 1.0
    term = base * v
    ii: int = 0
    s = 0.0   # total
    b = 0.0   # orig
    while b == 0 or s / b < _limit:
        ii += 1
        s += term
        b += base
        term *= v
    prt(f'loop2: for r={r*100:.2f}%, need {ii} years to exceed {_limit}')

def main():
    ''' main '''

    tryloop(0.03)

    prt('=' * 55)
    t = 1.5
    r = 0.05
    inc = 0.005
    prt(f'start from: {r} target: {t} inc: {inc}')
    for _ in range(5):
        loop2(r, t)
        r += inc
    prt('=' * 55)

if __name__ == '__main__':
    prt(__doc__)
    main()
