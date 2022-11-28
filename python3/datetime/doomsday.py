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
    if year <= 0:
        tdyear = date.today().year
    else:
        tdyear = year

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


def show_doom_number(year_list=None, full_list=False):
    ''' print out doom offset number within range '''
    td = date.today()

    if not year_list:
        CONTEXT = 2
        year_list = list(range(td.year-CONTEXT, td.year+CONTEXT+1))

    print("{")
    print('  "doom_number": {')

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
    parser.add_argument('-m', '--month', action='store_true', default=False,
        help='show magic number for each month')
    parser.add_argument("-f", "--full", action="store_true", default=False,
        help='show full variables')

    args = parser.parse_args()

    if args.test:
        print('perform self test...')
        TestDoomsDay.full_test()
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
            show_doom_number(args.years, args.full)
        return

    print('no arguments specified, use "-h" to see the help, will run default function...\n')
    #parser.print_help()
    show_doom_number()


if __name__ == '__main__':
    main()
