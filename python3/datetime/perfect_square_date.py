#!/usr/bin/env python3
# coding: utf-8

'''
to find perfect square date
the format of date is yyyymmdd (fill 0 if smaller than 10)
for example, 2015/3/9 will be 20150309

檢查八碼日期是否為完全平方數

'''

from math import sqrt
import sys
sys.path.insert(0, "..")
from myutil import is_leapyear

def logd(*args, **wargs):
    ''' logd '''
    print(*args, **wargs)

class Solution():
    ''' list a lot of date from 2000/1/1 to 2099/12/31
        and check if a perfect square
    '''
    YEAR_MIN = 2000
    YEAR_MAX = 2099

    def __init__(self):
        self.dates = []
        self.init_dates()
        self.answers1 = []
        self.answers2 = []

    @staticmethod
    def is_valid_date(y, m, d):
        ''' true if a valid date '''
        mod = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 0 < y <= 9999 and 1<=m<=12:
            if is_leapyear(y):
                mod[2] = 29
            return 1<=d<=mod[m]
        return False

    @staticmethod
    def is_int_valid_date(v):
        ''' is a valid date '''
        if not isinstance(v, int):
            logd(f'not a int {v}')
            return False
        y = v // 10000
        m = (v % 10000) // 100
        d = v - y*10000 - m*100
        #logd(f'{v=}, {y=},{m=},{d=}')
        if 1<=y<=9999 and 1<=m<=12 and 1<=d<=31:
            return Solution.is_valid_date(y, m, d)
        return False

    @staticmethod
    def date2int(y, m, d):
        ''' (yyyy, mm, dd) to integer '''
        the_str = f'{y:04d}{m:02d}{d:02d}'
        try:
            the_int = int(the_str)
            return the_int
        except ValueError:
            return 0

    def init_dates(self):
        ''' initial dates '''
        cnt = 0
        for y in range(self.YEAR_MIN, self.YEAR_MAX+1):
            for m in range(1, 13):
                for d in range(1, 32):
                    cnt += 1
                    if self.is_valid_date(y, m, d):
                        val = self.date2int(y, m, d)
                        if val > 0:
                            self.dates.append(val)

        logd(f'init_dates: test numbers: {cnt}, size of dates: {len(self.dates)}')
        logd(f'the first date is {self.dates[0]}, the last is {self.dates[-1]}')

    @staticmethod
    def dump_ans(the_list):
        ''' dump list '''
        for i in the_list:
            print(f'{i[0]} from {i[1]}')

    def test_dates(self):
        ''' test dates, collect all valid date and check
            if a perfect square
        '''
        logd('test dates...')
        cnt = 0
        for d in self.dates:
            cnt += 1
            r = sqrt(d)
            if r == int(r):
                self.answers1.append((d, int(r)))
        logd(f'test cnt: {cnt}, len: {len(self.answers1)}')
        self.dump_ans(self.answers1)

    def test_roots(self):
        ''' test roots
            get the smallest and the largest root, and check
            if a valid date
            fewer numbers to test
        '''
        logd('test_roots...')
        start_v = int(f'{self.YEAR_MIN}0101')
        end_v = int(f'{self.YEAR_MAX}1231')
        start_r = int(sqrt(start_v))
        if start_r * start_r < start_v:
            start_r += 1
        end_r = int(sqrt(end_v))
        cnt = 0
        logd(f'{start_r=} ... {end_r=}')
        for i in range(start_r, end_r+1):
            cnt += 1
            v = i*i
            if self.is_int_valid_date(v):
                #print(f'{v} from {i}')
                self.answers2.append((v, i))
        logd(f'test cnt: {cnt}, len: {len(self.answers2)}')
        self.dump_ans(self.answers2)

    def test_int(self):
        ''' fuck yeah '''
        assert self.is_int_valid_date(20151121)

    def action(self):
        ''' action '''
        self.test_dates()
        self.test_roots()
        #self.test_int()

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
