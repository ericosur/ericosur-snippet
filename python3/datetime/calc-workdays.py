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
from myutil import read_jsonfile, DefaultConfig  # type: ignore[import]
from myutil import is_leapyear, WhatNow, MyDebug, die  # type: ignore[import]
from loguru import logger
from rich import print as rprint

TAG = "CalcWork"
logd = logger.debug

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
        logd(f'max_year: {self.max_year}')
        logd(f'min_year: {self.min_year}')

    def calc(self, key):
        ''' calc '''
        max_mon, min_mon = "", ""
        max_day, min_day = 0, 99
        y_twenties = self.data[key]["month"]
        cnt = 0
        for p in y_twenties:
            for k, v in p.items():
                cnt += v
                self.all_days.append(v)
                if v > max_day:
                    max_mon, max_day = k, v
                if v < min_day:
                    min_mon, min_day = k, v

        y = self.data[key]["year"]
        if is_leapyear(y):
            r = cnt / 366 * 100
        else:
            r = cnt / 365 * 100
        if y == WhatNow().year:
            rprint(f"[yellow]{y}[/], {cnt}, {r:.2f}%,", end='  ')
        else:
            print(f"{y}, {cnt}, {r:.2f}%,", end='  ')
        print(f'{max_mon}, {max_day},', end='  ')
        print(f'{min_mon}, {min_day}')

    def calc_alldays(self):
        ''' about all days '''
        sz = len(self.all_days)
        t = sum(self.all_days)
        avg = float(t) / float(sz)
        rprint(f'\nTotal working days: {sz}, avg {avg:.2f} per month')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        from_year = obj.min_year
        to_year = obj.max_year
        print(f'From {from_year} to {to_year}\n')
        print("year  sum  ratio    max m/d   min m/d")
        for y in range(from_year, to_year+1):
            k = f'year{y}'
            obj.calc(k)
        obj.calc_alldays()

def main():
    ''' main '''
    CalcWork.run()

if __name__ == '__main__':
    main()
