#!/usr/bin/env python3
# coding: utf-8
#

''' just call dow '''

import sys
from datetime import date
from doomsday import dow

def check_and_call(dt):
    ''' input str list, and return dow '''
    dt = list(map(int, dt))
    #print(dt)
    return dow(dt[0], dt[1], dt[2])

def main(dt):
    ''' main '''
    if dt is None:
        td = date.today()
        tdow = int(td.weekday() + 1) % 7
        print('today: {}, dow: {}'.format(td, tdow))
        return

    try:
        ans = check_and_call(dt)
        print('{}/{}/{}: {}'.format(dt[0], dt[1], dt[2], ans))
    except ValueError as e:
        print('ValueError:', e)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        main(None)
    elif len(sys.argv) == 4:
        main(sys.argv[1:])
    else:
        print('dow_caller.py yy mm dd')