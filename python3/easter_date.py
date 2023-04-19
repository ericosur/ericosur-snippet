#!/usr/bin/python3
# coding: utf-8

'''
Anonymous Gregorian algorithm
https://en.wikipedia.org/wiki/Date_of_Easter

http://www.oremus.org/liturgy/etc/ktf/app/easter.html
'''

import datetime

def calculate_easter(year):
    ''' Calculate the date of Easter Sunday for the given year '''
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    # Return the date of Easter Sunday as a datetime object
    return datetime.date(year, month, day)

def main():
    ''' main '''
    def _show(y):
        print(calculate_easter(y))

    for y in range(2018, 2029):
        _show(y)

if __name__ == '__main__':
    main()
