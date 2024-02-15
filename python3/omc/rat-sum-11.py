#!/usr/bin/env python3
# coding: utf-8

'''
need Rational of sympy

* using greedy algorithm to solve egyptian fraction,
  the answer is not always optimized

* using sympy.Rational to do fraction calculation
  Rational: p / q

'''


from sympy import Rational

def test(vals):
    target = Rational(11,10)
    s = 0
    for v in vals:
        t = Rational(1, v)
        s += t
    print(vals, s)
    if target - s == 0:
        print('ok')
        return True
    return False


def action():
    ''' action '''



def main():
    ''' main '''
    action()

if __name__ == '__main__':
    main()
