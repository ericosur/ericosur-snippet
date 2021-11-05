'''
useful functions to search specific value in a very large list
'''

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
