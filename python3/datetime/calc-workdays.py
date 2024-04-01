#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=wrong-import-position
#

'''
calculate total working days
'''

import sys
sys.path.insert(0, "..")
from myutil import read_jsonfile, DefaultConfig, print_stderr
from myutil import is_leapyear, clamp, WhatNow

class CalcWork():
    ''' calc work class '''
    DATA_FILE = 'working-days.json'
    DEBUG = False

    def __init__(self):
        self.conf = ""
        self.data = None
        self.max_year = None
        self.min_year = None
        self.all_days = []
        self._load_conf()

    def logd(self, *args, **kwargs):
        '''
        from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
        '''
        if self.DEBUG:
            print("[DEBUG] ", file=sys.stderr, end='')
            print(*args, file=sys.stderr, **kwargs)

    def _load_conf(self):
        ''' load conf '''
        datafile = DefaultConfig(self.DATA_FILE).get_default_config()
        self.logd('read data from:', datafile)
        if not datafile:
            print_stderr('[FAIL] config file not found')
            sys.exit(1)

        self.data = read_jsonfile(datafile)
        if not self.data:
            print_stderr('[FAIL] cannot load data')
            sys.exit(1)
        self.max_year = self.data['maxyear']
        self.min_year = self.data['minyear']


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
        if is_leapyear(y):
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
        print(f'{sz=}, {avg=:.2f}')

    @classmethod
    def run(cls):
        ''' run '''
        this_year = WhatNow().year
        obj = cls()
        from_year = clamp(this_year - 3, obj.min_year, obj.max_year)
        to_year = clamp(this_year + 3, obj.min_year, obj.max_year)
        print(f'from {from_year} to {to_year}')
        for y in range(from_year, to_year+1):
            k = f'year{y}'
            obj.calc(k)

def main():
    ''' main '''
    CalcWork.run()

if __name__ == '__main__':
    main()
