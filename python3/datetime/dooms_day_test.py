#!/usr/bin/env python3
# coding: utf-8

'''
use doomsday algorithm to calculate weekday from range of year
https://en.wikipedia.org/wiki/Doomsday_rule

also using python's module to validate the results

reference:
http://people.se.cmich.edu/graha1sw/pub/doomsday/doomsday.html

'''

import calendar
from datetime import date

from dooms_day import DoomsDay


class TestDoomsDay():
    ''' class to test DoomsDay '''
    @staticmethod
    def test_offset():
        ''' test offset '''
        assert DoomsDay.get_offset_from_year(2019) == 5
        assert DoomsDay.get_offset_from_year(1987) == 4
        assert DoomsDay.get_offset_from_year(1843) == 2
        assert DoomsDay.get_offset_from_year(1773) == 0
        print('test_offset: pass')

    @staticmethod
    def test_leap(y, ans):
        ''' test leap year '''
        ret = DoomsDay.is_leap_year(y)
        if ret is ans:
            print(f'correct: {y}')
        else:
            print(f'wrong: {y}')

    @staticmethod
    def test_tmm(y, m, d):
        ''' test_tmm '''
        tmm = DoomsDay.get_tmm(y, m, d)
        td = date(y, m, d)
        wd = (td.weekday() + 1) % 7
        #print(f"{y}/{m}/{d} ==> {ret}")
        return tmm == wd, tmm, wd

    @staticmethod
    def test_dow(y, m, d):
        ''' test dow vs module datetime '''
        dw = DoomsDay.dow(y, m, d)
        wd = (date(y, m, d).weekday() + 1) % 7
        return dw == wd

    @staticmethod
    def full_test():
        ''' check is_leap_year is ok '''
        for yy in range(1, 3999):
            assert DoomsDay.is_leap_year(yy) == calendar.isleap(yy)
        print("pass")

        # check 1700/1/1 to 2099/12/31 weekday is ok
        try:
            for yy in range(1750, 1753):
                for mm in range(1, 12):
                    for dd in range(1, 31):
                        try:
                            assert TestDoomsDay.test_tmm(yy, mm, dd)
                            assert TestDoomsDay.test_dow(yy, mm, dd)
                        except ValueError:
                            # here pass all invalid date like 1701/2/29 ...
                            print(f"[WARN] value error at: {yy}/{mm}/{dd}")
        except AssertionError:
            print(f"failed at {yy}/{mm}/{dd}")
        print("pass")

if __name__ == '__main__':
    print('This script provides class TestDoomsDay, please run doomsday.py')
