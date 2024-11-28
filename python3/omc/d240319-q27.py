#!/usr/bin/env python3
# coding: utf-8

'''
Q27. 小明用六個自然數1，2，3，4，5，6 組成三個分數，
三個數字用來作分子，三個數字用來作分母，
然後他把這三個分數加起來得到和為 x / y, 已知x 與 y的最大公約數是1，求x+y的值。

'''

from itertools import combinations
#from utils import gcd
from sympy import Rational, gcd


def make_pairs():
    ''' make pairs '''
    nums = list(range(1,6+1))
    #print(nums)
    pairs = []
    for t in combinations(nums,2):
        (p, q) = t
        left = nums.copy()
        left.remove(p)
        left.remove(q)
        for u in combinations(left,2):
            (m, n) = u
            right = left.copy()
            right.remove(m)
            right.remove(n)
            #print(t, u, right)
            tmp = [list(t), list(u), list(right)]
            pairs.append(tmp)

    #print('len:', len(pairs))
    return pairs

def one_fraction(m, n):
    ''' one fraction '''
    return Rational(m, n)

def sum_fraction(p):
    ''' sum of egytian fraction '''
    total = 0
    total_rev = 0
    for v in p:
        [m, n] = v
        total += Rational(m, n)
        total_rev += Rational(n, m)
    return total, total_rev


def main():
    ''' main '''
    pairs = make_pairs()
    print(f'there are {len(pairs)}')
    xy = []
    for p in pairs:
        a, b = sum_fraction(p)
        aa = 0
        bb = 0
        if gcd(a.numerator, a.denominator)==1:
            aa = a.numerator + a.denominator
        if gcd(b.numerator, b.denominator)==1:
            bb = b.numerator + b.denominator
        #print(f'{p}, {a}:{aa}, {b}:{bb}')
        if aa not in xy:
            xy.append(aa)
        if bb not in xy:
            xy.append(bb)
    xy.sort()
    print(len(xy), xy)

if __name__ == '__main__':
    main()
