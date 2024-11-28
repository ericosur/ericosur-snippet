#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo days delta
'''

from datetime import datetime, timedelta


def translate_weekday(w: int):
    '''
    in module datetime, return value of d.weekday() monday is 0, sunday is 6
    translate it to sunday = 0, monday = 1, ..., saturday = 6
    '''
    if 0 <= w <= 6:
        t = w + 1
        t = t % 7
        return t
    raise ValueError("value out of range")

def days_between(dt, offday):
    ''' show days between '''

    # set start_date as specified date
    print(f"start_date: {dt}")

    # define offset
    offset = timedelta(days=offday)
    print(f"timedelta: {offset}")

    new_date = dt + offset
    wd = translate_weekday(new_date.weekday())
    print(f"new_date: {new_date}, weekday: {wd}")


def main():
    '''main function'''
    print('note: 0 is sunday, 1 is monday, and 6 is staturday')
    days_between(datetime(2023,10,16,13,30), 60)
    print()
    days_between(datetime.today(), 60)


if __name__ == '__main__':
    main()
