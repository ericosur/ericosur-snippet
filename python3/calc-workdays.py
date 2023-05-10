#!/usr/bin/env python3
# coding: utf-8
#

'''
calculate total working days
'''

import os
import sys
from myutil import read_jsonfile, get_home

class CalcWork():
    ''' calc work class '''
    def __init__(self):
        self.conf = ""
        self.data = None
        self._load_conf()

    def _load_conf(self):
        ''' load conf '''
        h = get_home()
        p = h + '/Private/working-days.json'
        if os.path.exists(p):
            self.data = read_jsonfile(p)
        else:
            print('[ERROR] config not found:', p)
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
                if v > max_day:
                    max_mon = k
                    max_day = v
                if v < min_day:
                    min_mon = k
                    min_day = v

        y = self.data[key]["year"]
        r = cnt / 365 * 100
        print(f"for year: {y}, count: {cnt}, ratio: {r:.2f}%")
        print(f'max_mon:{max_mon}, max_day:{max_day}')
        print(f'min_mon:{min_mon}, min_day:{min_day}')

def main():
    ''' main '''
    calc = CalcWork()
    for c in ["year2019", "year2020", "year2021", "year2022"]:
        calc.calc(c)

if __name__ == '__main__':
    main()
