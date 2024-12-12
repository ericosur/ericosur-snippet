#!/usr/bin/env python3
# coding: utf-8
#

''' just call dow
    note it is invalid before 1752-Sep-14, dow() uses the new
    rule for all dates before that day.
'''

import sys
from datetime import date
from dooms_day import DoomsDay
sys.path.insert(0, '../../')
sys.path.insert(0, 'python3')
from myutil import prt

WEEKDAY_NOTE = '0: Sun, 1: Mon, 2: Tue..., 6: Sat'

def check_and_call(dt: list[str]) -> int:
    ''' input a list of string, and return dow
    '''
    dt = list(map(int, dt))
    #prt(dt)
    return DoomsDay.dow(dt[0], dt[1], dt[2])

def run_demo():
    ''' demo '''
    prt('demo: Use date.today().weekday()...')
    td = date.today()
    tdow = int(td.weekday() + 1) % 7  # calibrate to 0 is Sun, 6 is Sat
    prt(f'today: {td}, dow: {tdow}')
    prt('# of week:', td.strftime("%V"))

def main(dt: list[str]):
    ''' main '''
    prt('Note:', WEEKDAY_NOTE)

    if dt is None:
        run_demo()
        exit(0)

    try:
        ans = check_and_call(dt)
        prt(f'{dt[0]}/{dt[1]}/{dt[2]}: {ans}')
    except ValueError as e:
        prt('ValueError:', e)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        prt('usage: dow_caller.py yyyy mm dd\n')
        main(None)
    elif len(sys.argv) == 4:
        main(sys.argv[1:])
