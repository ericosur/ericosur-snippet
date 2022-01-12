#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
demo yesterday
'''

from __future__ import print_function
import datetime
import calendar

def add_months(sourcedate, months):
    '''
    https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library
    may use +1, -1
    '''
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def main():
    ''' main '''
    start = datetime.datetime(2020, 12, 21)
    b = 31
    while b <= 240:
        print(f'{b}: {start}')
        start = add_months(start, 1)
        b += 1


if __name__ == '__main__':
    main()
