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
about 14 year we could doulbe the base

'''

def tryloop(r: float, _limit=2.0):
    ''' tryloop '''
    assert r > 0.0
    assert r < 1.0
    v = 1.0 + r
    ii = 0
    while v < _limit:
        ii += 1
        v *= 1 + r
    print('tryloop: for r={:.2f}%, need {} years to exceed {}'.format(r*100, ii, _limit))

def loop2(r: float, _limit=2.0):
    ''' loop2 '''
    assert r > 0.0
    assert r < 1.0

    v = 1 + r
    base = 1
    term = base * v
    ii = 0
    s = 0   # total
    b = 0   # orig
    while b == 0 or s / b < _limit:
        ii += 1
        s += term
        b += base
        #print('y{}: {} vs {:.3f}'.format(ii, b, s))
        term *= v
    print('loop2: for r={:.2f}%, need {} years to exceed {}'.format(r*100, ii, _limit))

def main():
    ''' main '''

    tryloop(0.03)

    print('=' * 40)
    t = 1.5
    r = 0.05
    inc = 0.005
    print('start from: {} target: {} inc: {}'.format(r, t, inc))
    for _ in range(5):
        loop2(r, t)
        r += inc

if __name__ == '__main__':
    print(__doc__)
    main()
