#!/usr/bin/python3
# coding: utf-8

''' count char in a string '''

from __future__ import print_function
from itertools import groupby
from random import randint

def get_freq(s: str):
    ''' get frequency, got a dict with key and frequency '''
    cc = sorted(list(s))
    d = {}
    for c in cc:
        if c == ' ':    # skip space
            continue
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for k in sorted(d.keys()):
        print('{}: {}, '.format(k, d[k]), end='')

def test_group(a: list):
    ''' test group returns a dict '''
    d = {}
    for key, group in groupby(a):
        d[key] = len(list(group))
    return d

def test_freq(a: list):
    ''' groupby oneliner a list with frequency '''
    f = [len(list(group)) for key, group in groupby(a)]
    return f

def gen_list(n: int, lower=1, upper=9):
    ''' gen a sorted list of int with n elements '''
    a = [randint(lower, upper) for _ in range(n)]
    return sorted(a)

def test1():
    ''' test #1 '''
    s = 'the quick brown fox jumps over the lazy dog'
    get_freq(s)

def test2():
    ''' test #2 '''
    a = gen_list(30)
    print(test_freq(a))
    print(test_group(a))


def main():
    ''' main '''
    test1()


if __name__ == '__main__':
    main()
