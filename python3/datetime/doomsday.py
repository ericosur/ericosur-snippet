#!/usr/bin/env python3
# coding: utf-8

'''
use doomsday algorithm to calculate weekday from range of year
https://en.wikipedia.org/wiki/Doomsday_rule

also using python's module to validate the results

reference:
http://people.se.cmich.edu/graha1sw/pub/doomsday/doomsday.html

'''

import argparse
import calendar
from datetime import date
import sys

def eprint(*args, **kwargs):
    ''' print to stderr '''
    print(*args, file=sys.stderr, **kwargs)

def is_leap_year(y):
    ''' is **y** a leap year? '''
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# copy from C/dow/
def dow(y, m, d):
    '''
    calculate weekday without any module
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
    #print("y: {} doom:{}".format(year, s))
    return int(s)

def test_offset():
    ''' test offset '''
    assert get_offset_from_year(2019) == 5
    assert get_offset_from_year(1987) == 4
    assert get_offset_from_year(1843) == 2
    assert get_offset_from_year(1773) == 0
    print('pass')

def test_leap(y, ans):
    ''' test leap year '''
    ret = is_leap_year(y)
    if ret is ans:
        print(f'correct: {y}')
    else:
        print(f'wrong: {y}')

def get_month_modifier(year):
    ''' get month modifier of specified year '''
    arr = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    if is_leap_year(year):
        arr[0] += 1
        arr[1] += 1
    #print(f"arr: {arr}")
    return arr

'''
example
1) weekday of 2022/5/04
year 2022 doom number is 6
month 5 doom number is 9
so, 4 - 6 - 9 = -11, plus 7 plut 7 get 3 (Wed)

2) weekday of 2020/6/17
year 2020 doom number is 1
month 6 doom number is 6
so, 17 - 1 - 6 = 10, mod 7 got 3 (Wed)

'''
def get_tmm(year, month, day):
    ''' get weekday by using doomsday method '''
    dm = get_doom_num(year)
    modifier = get_month_modifier(year)[month-1]
    tmp = day - modifier - dm
    while tmp < 0:
        tmp += 7
    return int(tmp % 7)

def test_dow(y, m, d):
    ''' test dow vs module datetime '''
    dw = dow(y, m, d)
    wd = (date(y, m, d).weekday() + 1) % 7
    return dw == wd

def test_tmm(y, m, d):
    ''' test_tmm '''
    tmm = get_tmm(y, m, d)
    td = date(y, m, d)
    wd = (td.weekday() + 1) % 7
    #print(f"{y}/{m}/{d} ==> {ret}")
    return tmm == wd, tmm, wd


def full_test():
    ''' check is_leap_year is ok '''
    for yy in range(1, 3999):
        assert is_leap_year(yy) == calendar.isleap(yy)
    print("pass")

    # check 1700/1/1 to 2099/12/31 weekday is ok
    try:
        for yy in range(1750, 1753):
            for mm in range(1, 12):
                for dd in range(1, 31):
                    try:
                        assert test_tmm(yy, mm, dd)
                        assert test_dow(yy, mm, dd)
                    except ValueError:
                        # here pass all invalid date like 1701/2/29 ...
                        print(f"[WARN] value error at: {yy}/{mm}/{dd}")
    except AssertionError:
        print(f"failed at {yy}/{mm}/{dd}")
    print("pass")

def show_month_magic_number(year=-1, show_header=True):
    ''' display magic number for this year '''
    if year <= 0:
        tdyear = date.today().year
    else:
        tdyear = year

    ret = get_month_modifier(tdyear)

    # output as json
    #print('If leap year, Feb magic number will be 1')
    if show_header:
        print("{")
    print('  "month_magic": {')
    print(f'    "year": {tdyear},')
    print(f'    "month_magic": {ret},')
    for i in range(11):
        print(f'    "{calendar.month_name[i+1]}": {ret[i]},')
    print(f'    "{calendar.month_name[12]}": {ret[11]}')
    print("  }")
    if show_header:
        print('}')


def show_doom_number(year_list=None, full_list=False):
    ''' print out doom offset number within range '''
    td = date.today()

    if not year_list:
        CONTEXT = 2
        year_list = list(range(td.year-CONTEXT, td.year+CONTEXT+1))

    print("{")
    print('  "doom_number": {')
    for yy in year_list:
        doomv = get_doom_num(yy)
        if yy == td.year:
            print('\x1b[33m', end='')
        print(f'    "year_{yy}": {doomv},')
        if yy == td.year:
            print('\x1b[00m', end='')

        if full_list:
            print("  },")
            show_month_magic_number(yy, show_header=False)

    print("}")

def main():
    ''' main '''

    # define argparse
    parser = argparse.ArgumentParser(description='shows doomsday number for specified years')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("years", metavar='year', type=int, nargs='*',
        help="specify year, like 2022")
    parser.add_argument('-t', '--test', action='store_true', default=False,
        help='perform self test')
    parser.add_argument('-m', '--month', action='store_true', default=False,
        help='show magic number for each month')
    parser.add_argument("-f", "--full", action="store_true", default=False,
        help='show full variables')
    # parser.add_argument("-v", "--verbose", action='store_true', default=False,
    #     help='verbose mode')

    # define the required args
    # requiredNamed = parser.add_argument_group('required named arguments')
    # requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    args = parser.parse_args()

    if args.test:
        print('perform self test...')
        full_test()
        return

    if args.month:
        # show magic number for each month
        if args.years:
            eprint('[WARN] the specified years are ignored\n')
        show_month_magic_number()
        return

    if args.years:
        if len(args.years) > 1 and args.full:
            eprint("[WARN] only the first one arg will be used")
            show_doom_number([args.years[0]], args.full)
        else:
            show_doom_number(args.years)
        return

    print('no arguments specified, use "-h" to see the help, will run default function...\n')
    #parser.print_help()
    show_doom_number()


if __name__ == '__main__':
    main()
