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
from myutil import read_jsonfile, DefaultConfig
from myutil import is_leapyear, clamp, WhatNow, MyDebug, die

TAG = "CalcWork"

class CalcWork(MyDebug):
    ''' calc work class '''
    DATA_FILE = 'working-days.json'

    def __init__(self):
        super().__init__(False)  # MyDebug
        self.conf = ""
        self.data = None
        self.max_year = None
        self.min_year = None
        self.all_days = []
        self._load_conf()

    def _log(self, *args, **wargs):
        ''' my own log '''
        if 'tag' not in wargs:
            wargs['tag'] = TAG
        self.logd(*args, **wargs)

    def _load_conf(self):
        ''' load conf '''
        self._log("_load_conf()...", tag=TAG)
        datafile = DefaultConfig(self.DATA_FILE, debug=False).get_default_config()
        self._log(f'read data from: {datafile}', tag=TAG)
        if not datafile:
            die('[FAIL] config file not found', self.DATA_FILE)
            return

        self.data = read_jsonfile(datafile)
        if not self.data:
            die('[FAIL] cannot load data')
            return

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
