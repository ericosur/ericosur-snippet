#!/usr/bin/env python3
#coding: utf-8

'''

use datetime to check possible year of which July 1st is on Monday

note: the calculation of weekday is implementation by dow(),
not by datetime.weekday(), thus no need to import datetime

'''

try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
from be_prepared import get_thisyear

logd = logger.debug if USE_LOGGER else print
prt = rprint if USE_RICH else print

def dow(year: int, month: int, day: int) -> int:
    '''
    calculate weekday without any module
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    '''
    (y, m, d) = (year, month, day)
    if m < 3:
        d += y
        y -= 1
    else:
        d += y - 2
    return (23*m//9+d+4+y//4-y//100+y//400)%7

def main():
    ''' main '''
    w = dow(2025, 3, 3)
    prt(f'2025 Mar 3rd is {w}')
    assert w == 1
    for y in range(2010, get_thisyear()+1):
        if dow(y, 7, 1) == 1:
            prt(f'{y} July 1st is on Monday')
    for y in range(2010, get_thisyear()+10):
        if dow(y, 2, 10) == 5:
            prt(f'{y} Feb 10th is on Friday')

if __name__ == '__main__':
    main()
