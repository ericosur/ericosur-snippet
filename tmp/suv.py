#!/usr/bin/env python3

'''
a demo to use sympy
reference from: http://blog.ez2learn.com/2009/08/25/sympy/
'''

from sympy import Symbol, solve, pprint

def main():
    ''' main '''
    p1x = Symbol('p1x')
    p1y = Symbol('p1y')

    p2x = Symbol('p2x')
    p2y = Symbol('p2y')

    ux = Symbol('ux')
    uy = Symbol('uy')

    vx = Symbol('vx')
    vy = Symbol('vy')

    s = Symbol('s')
    t = Symbol('t')

    fx = p1x - p2x + s*ux - t*vx
    fy = p1y - p2y + s*uy - t*vy

    sol = solve((fx, fy), s, t)

    print('s:')
    pprint(sol[s])

    print('t:')
    pprint(sol[t])

if __name__ == '__main__':
    main()
