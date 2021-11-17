#!/usr/bin/python3
# coding: utf-8
#

'''
calculate total working days
'''

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
        self.data = read_jsonfile(p)

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
    calc.calc("year2021")
    calc.calc("year2022")

if __name__ == '__main__':
    main()
