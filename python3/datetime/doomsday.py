#!/usr/bin/env python3
# coding: utf-8

'''
This script uses class DoomsDay and TestDoomsDay, and provides CLI.
'''

import argparse
import calendar
from datetime import date
import sys
from dooms_day import DoomsDay
from dooms_day_test import TestDoomsDay

def eprint(*args, **kwargs):
    ''' print to stderr '''
    print(*args, file=sys.stderr, **kwargs)


def show_month_magic_number(year=-1, show_header=True):
    ''' display magic number for this year '''
    # if year <= 0:
    #     tdyear = date.today().year
    # else:
    #     tdyear = year
    tdyear = date.today().year if year <=0 else year
    ret = DoomsDay.get_month_modifier(tdyear)

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

def make_year_list(base_year=0, opt='c', year_range=5):
    ''' fill year list as required
    if base_year is 0, use this year
    opt will be
        - c (context, 0: only itself, 1: a1,b1, 2: a2,b2)
        - a (after, included and year_range years)
        - b (before, included and year_range years)
        - None, use this year
    '''
    if year_range < 0:
        raise ValueError("year_range MUST NOT smaller than 0")

    start_year = date.today().year if base_year <= 0 else base_year

    answer = []
    if opt == 'c':
        context = year_range
        answer = list(range(start_year-context, start_year+context+1))
    elif opt == 'a':
        count = year_range
        answer = list(range(start_year, start_year+count+1))
    elif opt == 'b':
        count = year_range
        answer = list(range(start_year-count, start_year+1))
    else:
        raise ValueError("option not supported")

    return answer

def test_year_list():
    ''' test make_year_list '''
    try:
        ret = make_year_list(0, 'c', 0)
        assert ret == [2022]
        ret = make_year_list(0, 'c', 1)
        assert ret == [2021, 2022, 2023]
        ret = make_year_list(0, 'c', 2)
        assert ret == [2020, 2021, 2022, 2023, 2024]
        try:
            ret = make_year_list(0, 'c', -1)
            assert not ret
        except ValueError:
            print("exception caught as expected, invalid year_range")

        ret = make_year_list(0, 'a', 0)
        assert ret == [2022]
        ret = make_year_list(0, 'a', 1)
        assert ret == [2022, 2023]
        try:
            ret = make_year_list(0, 'a', -1)
            assert not ret
        except ValueError:
            print("exception caught as expected, invalid year_range")

        ret = make_year_list(0, 'b', 0)
        assert ret == [2022]
        ret = make_year_list(0, 'b', 1)
        assert ret == [2021, 2022]
        ret = make_year_list(0, 'b', 2)
        assert ret == [2020, 2021, 2022]
        try:
            ret = make_year_list(0, 'b', -1)
            assert not ret
        except ValueError:
            print("exception caught as expected, invalid year_range")

        ret = make_year_list(1895, 'c', 0)
        assert ret == [1895]
        ret = make_year_list(1895, 'c', 3)
        assert ret == [1892, 1893, 1894, 1895, 1896, 1897, 1898]
        ret = make_year_list(1949, 'a', 3)
        assert ret == [1949, 1950, 1951, 1952]
        ret = make_year_list(1900, 'b', 3)
        assert ret == [1897, 1898, 1899, 1900]
        try:
            ret = make_year_list(0, 'd', 0)
        except ValueError:
            print("exception caught as expected, invalid option")

    except AssertionError as err:
        print("AssertionError: ret:", ret, "\nerr:", err)

    print("test done...")


def show_doom_number(year_list=None, full_list=False):
    ''' print out doom offset number within range '''
    # if year_list is empty, add default value
    if not year_list:
        if full_list:
            year_list = make_year_list(0, 'c', 0)
        else:
            year_list = make_year_list(0, 'c', 2)

    print("{")
    print('  "doom_number": {')

    td = date.today()
    list_size = len(year_list)
    for idx, yy in enumerate(year_list):
        doomv = DoomsDay.get_doom_num(yy)
        if yy == td.year:
            print('\x1b[33m', end='')
        print(f'    "year_{yy}": {doomv}', end='')
        if idx < list_size - 1:
            print(',')
        else:
            print()

        if yy == td.year:
            print('\x1b[00m', end='')

        if full_list:
            print("  },")
            show_month_magic_number(yy, show_header=False)

    if not full_list:
        print("  }")
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
    parser.add_argument('-T', '--Test', action='store_true', default=False,
        help='test make_year_list')
    parser.add_argument('-m', '--month', action='store_true', default=False,
        help='show magic number for each month')
    parser.add_argument("-f", "--full", action="store_true", default=False,
        help='show full variables')
    parser.add_argument("-c", "--context", type=int, help="context years")
    parser.add_argument("-a", "--after", type=int, help="after years")
    parser.add_argument("-b", "--before", type=int, help="before years")

    args = parser.parse_args()

    if args.test:
        print('perform self test...')
        TestDoomsDay.full_test()
        return
    if args.Test:
        test_year_list()
        return

    if args.month:
        # show magic number for each month
        yy = -1
        if args.years:
            eprint('[WARN] only the first specified year is used\n')
            yy = args.years[0]

        show_month_magic_number(yy)
        return

    if args.context or args.after or args.before:
        yy = -1
        if args.years:
            yy = args.years[0] if args.years[0] else 0

        if args.context:
            ret = make_year_list(yy, "c", args.context)

        if args.after:
            ret = make_year_list(yy, "a", args.after)

        if args.before:
            ret = make_year_list(yy, "b", args.before)

        show_doom_number(ret, args.full)
        return

    if args.years:
        if len(args.years) > 1 and args.full:
            eprint("[WARN] only the first one arg will be used")
            args.years = args.years[:1]
        show_doom_number(args.years, args.full)
        return

    print('no arguments specified, use "-h" to see the help, will run default function...\n')
    #parser.print_help()
    show_doom_number(None, args.full)


if __name__ == '__main__':
    main()
