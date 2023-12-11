#!/usr/bin/env python3
# coding: utf-8

'''
bisect demo:
https://docs.python.org/zh-tw/3/library/bisect.html

At [test_exist.py](../prime/test_exist.py), it demos how slow "item in a large list".

'''

import random
from bisect import bisect_left, bisect_right


def index(a: list, x: int):
    ''' return index of the leftmost value exactly equal to x '''
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

def find_lt(a: list, x: int):
    ''' Find rightmost value less than x '''
    i = bisect_left(a, x)
    if i:
        return a[i-1], i-1
    raise ValueError

def find_le(a: list, x: int):
    ''' Find rightmost value less than or equal to x '''
    i = bisect_right(a, x)
    if i:
        return a[i-1], i-1
    raise ValueError

def find_gt(a: list, x: int):
    ''' Find leftmost value greater than x '''
    i = bisect_right(a, x)
    if i != len(a):
        return a[i], i
    raise ValueError

def find_ge(a: list, x: int):
    ''' Find leftmost item greater than or equal to x '''
    i = bisect_left(a, x)
    if i != len(a):
        return a[i], i
    raise ValueError

def test(x):
    ''' test '''
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
         31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
         73, 79, 83, 89, 97]
    i = index(a, x)
    if i != -1:
        print(f'{x} found at index {i}')
        return
    try:
        m, _ = find_le(a, x)
        p, _ = find_ge(a, x)
        print(f'{x} between {m} and {p}')
    except ValueError:
        print(f'something wrong for {x}, OOB?')


def main():
    ''' main '''
    repeat = 10
    for _ in range(repeat):
        x = random.randint(1, 101)
        test(x)


if __name__ == '__main__':
    main()
