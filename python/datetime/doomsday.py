#!/usr/bin/env python3
# coding: utf-8

'''
use doomsday algorithm to calculate weekday from range of year
https://en.wikipedia.org/wiki/Doomsday_rule

also using python's module to validate the results
'''

from datetime import date
import calendar

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def get_doom_num(y):
    offset = 0
    if y >= 2000:
        offset = 5
    elif y >= 1900:
        offset = 4
    elif y >= 1800:
        offset = 2
    elif y >= 1700:
        offset = 0
    year = y
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
    #print("y: {} doom:{}".format(year, s))
    return int(s)

def test_leap(y, ans):
    ret = is_leap_year(y)
    if ret is ans:
        print('correct: {}'.format(y))
    else:
        print('wrong: {}'.format(y))

def get_month_modifier(year):
    arr = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    if is_leap_year(year):
        arr[0] += 1
        arr[1] += 1
    #print("arr: {}".format(arr))
    return arr

def get_tmm(year, month, day):
    dm = get_doom_num(year)
    modifier = get_month_modifier(year)[month-1]
    tmp = day - modifier - dm
    while tmp < 0:
        tmp += 7
    return int(tmp % 7)

def test_tmm(y, m, d, ans):
    ret = tmm(y, m, d)
    ret = ret
    print("{}/{}/{} ==> {}".format(y, m, d, ret))

def full_test():
    # check is_leap_year is ok
    for yy in range(1, 3999):
        assert is_leap_year(yy) == calendar.isleap(yy)
    print("pass")

    # check 1700/1/1 to 2099/12/31 weekday is ok
    try:
        for yy in range(1700, 2099):
            for mm in range(1, 13):
                for dd in range(1, 32):
                    try:
                        td = date(yy, mm, dd)
                        tmm = int(get_tmm(yy, mm, dd))
                        # for date.weekday(), monday = 0, sunday = 6
                        wd = int((td.weekday() + 1) % 7)
                        assert tmm == wd
                    except ValueError:
                        # here pass all invalid date like 1701/2/29 ...
                        #print("[WARN] value error at: {}/{}/{}".format(yy, mm, dd))
                        pass
    except AssertionError:
        print("failed at yy{}, tmm{} vs wd{}".format(yy, tmm, wd))
    print("pass")


if __name__ == '__main__':
    full_test()
    td = date.today()
    RANGE = 2
    from_year = td.year - RANGE
    to_year = td.year + RANGE
    yy = from_year
    while yy <= to_year:
        doomv = get_doom_num(yy)
        print("doom number for year {} = {}".format(yy, doomv))
        yy += 1
