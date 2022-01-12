#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
demo days delta
'''

from datetime import timedelta, datetime

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

def main():
    '''main function'''
    # set start_date as specified date
    start_date = datetime(2021, 10, 25, 10, 00)
    print(f"start_date: {start_date}")

    # define offset
    offset = timedelta(days=84)
    print(f"timedelta: {offset}")

    new_date = start_date + offset
    wd = translate_weekday(new_date.weekday())
    print(f"new_date: {new_date}, weekday: {wd}")

    print('note: 0 is sunday, 1 is monday, and 6 is staturday')

if __name__ == '__main__':
    main()
