#!/usr/bin/env python3
# coding: utf-8

'''
calculate total working days
'''

import sys
from myutil import read_jsonfile, DefaultConfig, print_stderr


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

    @staticmethod
    def is_leapyear(y):
        ''' is **y** a leap year? '''
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

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
        print(f'{sz=}, {avg=:.2f}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        print(f'{obj.min_year=}\t{obj.max_year=}')
        for y in range(obj.min_year, obj.max_year+1):
            k = f'year{y}'
            obj.calc(k)

def main():
    ''' main '''
    CalcWork.run()

if __name__ == '__main__':
    main()
