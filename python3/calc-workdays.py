#!/usr/bin/env python3
# coding: utf-8

'''
calculate total working days
'''

import os
import sys
from myutil import read_jsonfile, get_home

class CalcWork():
    ''' calc work class '''
    DATA_FILE = 'working-days.json'
    DEBUG = True

    def __init__(self):
        self.conf = ""
        self.data = None
        self.max_year = None
        self.min_year = None
        self.all_days = []
        self._load_conf()

    @staticmethod
    def is_leapyear(y):
        ''' is **y** a leap year? '''
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def _load_conf(self):
        ''' load conf '''
        homedir = get_home()
        try_paths = [self.DATA_FILE]
        p = os.path.join(homedir, self.DATA_FILE)
        try_paths.append(p)
        p = os.path.join(homedir, 'Private', self.DATA_FILE)

        for x in try_paths:
            if os.path.exists(x):
                if self.DEBUG:
                    print('read data from:', x)
                self.data = read_jsonfile(x)
                self.max_year = self.data['maxyear']
                self.min_year = self.data['minyear']
                return

        print('[ERROR] config file not found')
        sys.exit(1)

    def calc(self, key):
        ''' calc '''
        max_mon = ""
        max_day = 0
        min_mon = ""
        min_day = 99
        y_twenties = self.data[key]["month"]
        cnt = 0
        for p in y_twenties:
            for k, v in p.items():
                cnt += v
                self.all_days.append(v)
                if v > max_day:
                    max_mon = k
                    max_day = v
                if v < min_day:
                    min_mon = k
                    min_day = v

        y = self.data[key]["year"]
        if self.is_leapyear(y):
            r = cnt / 366 * 100
        else:
            r = cnt / 365 * 100
        print(f"year: {y}, count: {cnt}, ratio: {r:.2f}%")
        print(f'max: {max_mon}, {max_day}')
        print(f'min: {min_mon}, {min_day}')
        self.calc_alldays()

    def calc_alldays(self):
        ''' about all days '''
        sz = len(self.all_days)
        t = sum(self.all_days)
        avg = float(t) / float(sz)
        print(f'{sz=}, {avg=}')

    @classmethod
    def run(cls):
        ''' run '''
        calc = cls()
        print(f'{calc.min_year=}\t{calc.max_year=}')
        for y in range(calc.min_year, calc.max_year+1):
            k = f'year{y}'
            calc.calc(k)

def main():
    ''' main '''
    CalcWork.run()

if __name__ == '__main__':
    main()
