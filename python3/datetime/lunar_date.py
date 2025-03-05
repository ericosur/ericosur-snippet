#!/usr/bin/env python3
# coding: utf-8
#

'''
try to use lunarcalendar

pip install LunarCalendar

use __lunar-find all 2025__ to find all festivals in 2025
use __lunar-find solarterm 2025__ to get all solar terms in 2025
'''


#import datetime
import itertools as it
import sys
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False

try:
    from lunarcalendar import Converter, DateNotExist, Lunar, Solar  # type: ignore[import]
    from lunarcalendar.festival import festivals  # type: ignore[import]
except ImportError:
    print('failed to import module lunarcalendar')
    sys.exit(1)

from be_prepared import get_thisyear  # type: ignore[import]

logd = logger.debug if USE_LOGGER else print
prt = rprint if USE_RICH else print

class Solution:
    ''' solution '''
    def __init__(self, year=2020):
        self.year = year

    def get_year(self):
        ''' year '''
        return self.year

    def print_festival(self):
        ''' print festivals, using English or Chinese '''
        print(f"----- print all festivals on {self.year} in chinese: -----")
        for fest in festivals:
            print(fest.get_lang('zh_hant'), fest(self.year))

        #print("----- print all festivals on 2017 in english: -----")
        #for fest in festivals:
        #    print(fest.get_lang('en'), fest(2017))

    def action(self):
        ''' just go '''
        self.print_festival()

        # solar = Converter.Lunar2Solar(lunar)
        # print(solar)
        # lunar = Converter.Solar2Lunar(solar)
        # print(lunar)
        # print(lunar.to_date(), type(lunar.to_date()))
        # print(Lunar.from_date(datetime.date(2020, 1, 1)))

    @staticmethod
    def show_lunar_leap_date():
        '''
        test if lunar(year, month) is leap
        using itertools
        '''
        for n in it.product(list(range(2020, 2031)), list(range(1, 13))):
            try:
                (y, m) = n
                lunar = Lunar(y, m, 1, isleap=True)
                print(f'{lunar} => {lunar.to_date()}')
            except DateNotExist:
                logd(f'DateNotExist: {y} {m} is not a leap month')

    @staticmethod
    def show_someday():
        ''' show_someday '''
        def s2l(yy):
            ''' solar date to lunar date '''
            ss = Solar(yy, 2, 10)
            ll = Converter.Solar2Lunar(ss)
            print(f'{ss.to_date()} => {ll}')

        s2l(2012)
        prt('-' * 65)
        this_year = get_thisyear()
        for yy in range(this_year, this_year+10):
            s2l(yy)

def main():
    ''' main '''
    Solution.show_someday()

if __name__ == '__main__':
    main()
