#!/usr/bin/env python3
#
# pylint: disable=wrong-import-position
#

'''
calculate total working days
'''

import sys

try:
    from datetime_common import do_nothing, logd, prt  # type: ignore[import]

    from myutil import (  # type: ignore[import]
        DefaultConfig,
        WhatNow,
        die,
        is_leapyear,
        read_jsonfile,
    )
except ImportError as e:
    print("[FAIL] need myutil module from myutil package", e)
    sys.exit(1)

TAG = "CalcWork"

class CalcWork:
    ''' calc work class '''
    DATA_FILE = 'working-days.json'

    def __init__(self, _debug: bool=False):
        self.conf = ""
        self.data = None
        self.max_year = 2030
        self.min_year = 2000
        self.all_days = []
        self._debug = _debug
        self._log = logd if _debug else do_nothing
        self._load_conf()
        self.from_year = self.min_year if self.min_year else 2023
        self.to_year = self.max_year if self.max_year else WhatNow().year

    def _load_conf(self):
        ''' load conf '''
        self._log(f'[{TAG}] _load_conf()...')
        datafile = DefaultConfig(self.DATA_FILE, debug=False).get_default_config()
        self._log(f'[{TAG}] read data from: {datafile}')
        if not datafile:
            die('[FAIL] config file not found:', self.DATA_FILE)
            return

        self.data = read_jsonfile(datafile)
        assert self.data, '[FAIL] cannot load data'
        self._log(f'[{TAG}] data loaded, keys: {list(self.data.keys())}')
        self.max_year = self.data['maxyear']
        self.min_year = self.data['minyear']
        self._log(f'[{TAG}] max_year: {self.max_year}')
        self._log(f'[{TAG}] min_year: {self.min_year}')

    def calc(self, key):
        ''' calc '''
        max_mon, min_mon = "", ""
        max_day, min_day = 0, 99
        assert self.data is not None and key in self.data, f'[FAIL] key not found: {key}'
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
            prt(f"[yellow]{y}[/], {cnt}, {r:.2f}%,", end='  ')
        else:
            print(f"{y}, {cnt}, {r:.2f}%,", end='  ')
        print(f'{max_mon}, {max_day},', end='  ')
        print(f'{min_mon}, {min_day}')

    def calc_alldays(self):
        ''' about all days '''
        sz = len(self.all_days)
        t = sum(self.all_days)
        avg = float(t) / float(sz)
        prt(f'\nTotal months: {sz}, avg {avg:.2f} per month')

    def print_header(self):
        ''' print header '''
        prt(f'From {self.from_year} to {self.to_year}')
        prt("year  sum  ratio    max m/d   min m/d")
        prt("----  ---  -----    -------   -------")

    def print_years(self):
        ''' print years '''
        for y in range(self.from_year, self.to_year+1):
            k = f'year{y}'
            self.calc(k)
        self.calc_alldays()

    @classmethod
    def run(cls, _debug: bool=False):
        ''' run '''
        obj = cls(_debug)
        obj.print_header()
        obj.print_years()

    
if __name__ == '__main__':
    if len(sys.argv) > 1 and (sys.argv[1] == '--debug' or sys.argv[1] == '-d'):
        CalcWork.run(_debug=True)
    else:
        CalcWork.run()
