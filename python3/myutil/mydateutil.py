#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful utility functions without datetime
    for calculating some date time
'''

__VERSION__ = "2024.04.01"

def is_leapyear(y):
    ''' is **y** a leap year? '''
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def get_dow(y, m, d):
    '''
    calculate weekday without any module
    return 0 to 6, means sun, mon, tue, wed, thu, fri, sat
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    '''
    if m < 3:
        d += y
        y -= 1
    else:
        d += y - 2
    return (23*m//9+d+4+y//4-y//100+y//400)%7


def get_offset_from_year(y):
    ''' return offset of input year '''
    offset = 0
    r = (y // 100) % 4
    if r == 1:  # 1700, 1300
        offset = 0
    elif r == 2:    # 1800, 1400
        offset = 2
    elif r == 3:    # 1900, 1500
        offset = 4
    else:  # r == 0, 2000, 1600
        offset = 5
    return offset


def get_doom_num(y):
    ''' calculate doomsday number of specified year '''
    offset = get_offset_from_year(y)
    y = y % 100
    if y % 2:
        t0 = (y + 11) / 2
    else:
        t0 = y / 2
    t1 = 0
    if t0 % 2:
        t1 = t0 + 11
    else:
        t1 = t0
    r = (t1 + offset) % 7
    s = r % 7
    return int(s)
