#!/usr/bin/env python3
# coding: utf-8

'''
helper function to draw an indicator to show relative position between
three numbers (esp lower and upper are primes)

17
18 [m]  (between twin primes)
19

47
48 [#--_-]
53

32771
32773 [-#-_---]
32779

32771
32775 [---m---]
32779

32749
32760 .......m.......
32771

32749
32769 .............#.
32771

'''

MODNAME = 'makearrow'
__VERSION__ = '2023.10.31'


def _basic_check(lower, v, upper):
    ''' perform basic check '''
    if lower > upper or abs(upper - lower) < 2:
        raise ValueError
    if abs(lower-v) < 1 or abs(upper-v) < 1:
        raise ValueError

def _get_fivestop(cnt, step):
    ''' use _ to indicate five stop '''
    if (cnt+1)%5 == 0:
        return '_'
    return step

def _get_middlesign(is_middle):
    ''' return m if is_middle '''
    if is_middle:
        return 'm'
    return '#'


def make_arrow(lower, v, upper):
    '''
    generate indicator to show relationship between numbers
    '''

    _basic_check(lower, v, upper)

    # special case
    if upper - lower == 2:
        return "[m]  (between twin primes)"

    s = ''
    max_len = 15    # better if it is odd number
    step = '-'
    d = abs(upper - lower)
    is_middle = abs(upper - v) == abs(lower - v)
    if d < max_len:
        s = '['
        cnt = 1
        # left-hand-side
        for _ in range(abs(v-lower-1)):
            s += _get_fivestop(cnt, step)
            cnt += 1

        # the number v
        s += _get_middlesign(is_middle)
        cnt += 1

        # right-hand-side
        for _ in range(abs(v-upper)-1):
            s += _get_fivestop(cnt, step)
            cnt += 1

        s += ']'
        return s

    # make arrow by ratio
    step = "."
    r = int(abs(v-lower)/(upper-lower) * max_len)
    for i in range(max_len):
        if i == r:
            s += _get_middlesign(is_middle)
        else:
            s += step
    return s
