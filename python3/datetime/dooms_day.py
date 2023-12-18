#!/usr/bin/env python3
# coding: utf-8

'''
use doomsday algorithm to calculate weekday from range of year
https://en.wikipedia.org/wiki/Doomsday_rule

also using python's module to validate the results

reference:
http://people.se.cmich.edu/graha1sw/pub/doomsday/doomsday.html

example
    1) weekday of 2022/5/04
        year 2022 doom number is 6
        month 5 doom number is 9
        so, 4 - 6 - 9 = -11, plus 7 plut 7 get 3 (Wed)

    2) weekday of 2020/6/17
        year 2020 doom number is 1
        month 6 doom number is 6
        so, 17 - 1 - 6 = 10, mod 7 got 3 (Wed)

'''

class DoomsDay():
    ''' utility functions to provide doomsday number '''

    @staticmethod
    def is_leap_year(y):
        ''' is **y** a leap year? '''
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    @staticmethod
    def dow(y, m, d):
        '''
        calculate weekday without any module
        https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
        '''
        if m < 3:
            d += y
            y -= 1
        else:
            d += y - 2
        return (23*m//9+d+4+y//4-y//100+y//400)%7

    @staticmethod
    def get_offset_from_year(y):
        ''' return offset of input year '''
        offset = 0
        r = (y // 100) % 4
        if r == 1:  # 1700, 1300
            offset = 0
        elif r == 2:    # 1800, 1400
            offset = 2
        elif r == 3:    # 1900, 1500
            offset = 4
        else:  # r == 0, 2000, 1600
            offset = 5
        return offset

    @staticmethod
    def get_doom_num(y):
        ''' calculate doomsday number of specified year '''
        offset = DoomsDay.get_offset_from_year(y)
        y = y % 100
        if y % 2:
            t0 = (y + 11) / 2
        else:
            t0 = y / 2
        t1 = 0
        if t0 % 2:
            t1 = t0 + 11
        else:
            t1 = t0
        r = (t1 + offset) % 7
        s = r % 7
        #print("y: {} doom:{}".format(year, s))
        return int(s)

    @staticmethod
    def get_month_modifier(year):
        ''' get month modifier of specified year '''
        arr = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
        if DoomsDay.is_leap_year(year):
            arr[0] += 1
            arr[1] += 1
        #print(f"arr: {arr}")
        return arr

    @staticmethod
    def get_tmm(year, month, day):
        ''' get weekday by using doomsday method '''
        dm = DoomsDay.get_doom_num(year)
        modifier = DoomsDay.get_month_modifier(year)[month-1]
        tmp = day - modifier - dm
        while tmp < 0:
            tmp += 7
        return int(tmp % 7)

if __name__ == '__main__':
    print('This script provides class DoomsDay, please run doomsday.py')
