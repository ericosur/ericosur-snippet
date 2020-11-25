#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
to list black Friday
Here "black Friday" means date 13 for each month and it's Friday.
Not the "Black Friday" after the Thanksgiving
'''

from __future__ import print_function
from datetime import datetime, date


def get_blackfriday(from_year, to_year):
    '''
    list black friday by specifying from_year to to_year
    '''
    MIN_MONTH = 1
    MAX_MONTH = 12
    # 0:MON, 1:TUE, 2:WED, 3:THU, 4:FRI, 5:SAT, 6:SUN
    WEEKDAY_FRIDAY = 4

    for yr in range(from_year, to_year+1):
        for mnth in range(MIN_MONTH, MAX_MONTH+1):
            dd = datetime(yr, mnth, 13)
            if dd.weekday() == WEEKDAY_FRIDAY:
                print("Black Friday: ", get_date_str(dd))

def get_date_str(dd):
    ''' print date time by format '''
    return dd.strftime("%d %b %Y")


def main():
    ''' main function '''
    RANGE = 5
    today = date.today()
    from_y = today.year
    get_blackfriday(from_y, from_y+RANGE)


if __name__ == '__main__':
    #print(get_date_str(date.today()))
    main()
