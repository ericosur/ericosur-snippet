#!/usr/bin/env python3
# coding: utf-8

'''
This script uses class DoomsDay and TestDoomsDay, and provides CLI.
'''

import argparse
import sys
from datetime import date
from typing import List

# try to add my code snippet into python path
# sys.path.insert(0, '../')
# sys.path.insert(0, '../../')
# sys.path.insert(0, 'python3/')

USE_RICH = False
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    #print("[WARN] no rich.console to use")
    pass

try:
    from dooms_day import DoomsDay
    from dooms_day_test import TestDoomsDay
except ImportError:
    print('cannot import dooms_day, exit')
    sys.exit(1)

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
#    print('    "month_magic": {')
#    print(f'      "year": {tdyear},')
    print(f'    "month_magic": {ret},')
    # for i in range(11):
    #     print(f'      "{calendar.month_name[i+1]}": {ret[i]},')
    # print(f'      "{calendar.month_name[12]}": {ret[11]}')
    #print("    }")
    if show_header:
        print('}')

def make_year_list(base_year:int=0, opt='c', year_range=5) -> list:
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

def get_thisyear() -> int:
    ''' get this year '''
    return date.today().year

def show(color: str, msg: str) -> None:
    ''' show '''
    if USE_RICH:
        rprint(f'[{color}]{msg}')
    else:
        print(msg)

def get_year_color(yy: int, target_year: int) -> str:
    ''' return the color from the input year '''
    this_year = get_thisyear()
    ret_color = "white"
    if yy == this_year:
        if yy == target_year:
            ret_color = "red"
        else:
            ret_color = "green"
    elif yy==target_year:
        ret_color = "yellow"
    return ret_color

def show_doom_number(year_list=None, target:int=-1, full_list=False):
    ''' print out doom offset number within range '''
    # if year_list is empty, add default value
    if not year_list:
        if full_list:
            year_range = 0
        else:
            year_range = 3
        year_list = make_year_list(0, 'c', year_range)

    print("{")
    print('  "doom_number": [')

    for idx, yy in enumerate(year_list):
        doomv = DoomsDay.get_doom_num(yy)
        if full_list:
            print('  {')

        msg=f'    "year_{yy}": {doomv}'
        if idx!=len(year_list)-1 or full_list:
            msg += ','
        clr = get_year_color(yy, target)
        show(clr, msg)

        if full_list:
            show_month_magic_number(yy, show_header=False)
            msg = '  }'
            if idx!=len(year_list)-1:
                msg += ','
            print(msg)

    if not full_list:
        print("  }")
    else:
        print("  ]")
    print("}")

def prepare_values(year: int, after: int=0, before: int=0, radius: int=0) -> List[int]:
    ''' prepare values '''
    year = year if year is not None else get_thisyear()
    after = after if after is not None else 0
    before = before if before is not None else 0
    radius = radius if radius is not None else 0
    if after<0 or before<0 or radius<0:
        raise ValueError("value MUST be greater than 0")
    if radius!=0:
        if after!=0 or before!=0:
            print(f"CONFLICT: context({radius}) vs after({after})/before({before})")
            print("The value of context will override after and/or before")
        after, before = radius, radius
    upper = year + after
    lower = year - before
    if lower>upper:
        lower,upper = upper,lower
    vals = []
    for y in range(lower,upper+1):
        vals.append(y)
    return vals

def init_argparse():
    ''' argparse '''
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
    parser.add_argument("-C", "--context", type=int, help="context years")
    parser.add_argument("-A", "--after", type=int, help="after years")
    parser.add_argument("-B", "--before", type=int, help="before years")
    parser.add_argument("-x", "--extra", action="store_true", default=False,
        help='show extra info')

    args = parser.parse_args()
    return args

def main():
    ''' main '''
    args = init_argparse()

    if args.extra:
        print(f'''Extra info:
  Actually only the first three magic numbers (Jan/Feb/Mar) are special.
  The magic number for Mar is always 0. So:
    - if a leap year like 2024, they are (4, 1, 0).
      - use ```{sys.argv[0]} 2024 -m```
    - if a normal year like 2025, they are (3, 0, 0).
      - use ```{sys.argv[0]} 2025 -m```''')
        return
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
            if len(args.years) > 1:
                eprint('[WARN] only the first specified year is used\n')
            yy = args.years[0]
        show_month_magic_number(yy)
        return

    if args.context or args.after or args.before:
        yy = None
        if args.years:
            yy = args.years[0] if args.years[0] else 0
        ret = prepare_values(yy, args.after, args.before, args.context)
        show_doom_number(ret, target=yy, full_list=args.full)
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
