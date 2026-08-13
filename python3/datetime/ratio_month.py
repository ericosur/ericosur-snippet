#!/usr/bin/env python3

import argparse
import traceback

'''
ratio between a month
data plan count from (mm/dd, including) prev month 16 to this month 15
get the ratio as a reference for today usage

'''

from datetime import date, timedelta

from be_prepared import get_today
from datetime_common import prt


def test_dates():
    ''' test '''
    r = NextMonth.get_nextmonthdate(date(2023,2,28))
    assert r == date(2023,3,28)
    r = NextMonth.get_nextmonthdate(date(2023,1,29))
    assert r == date(2023,2,28)
    r = NextMonth.get_nextmonthdate(date(2024,1,29))
    assert r == date(2024,2,29)
    r = NextMonth.get_nextmonthdate(date(2023,11,29))
    assert r == date(2023,12,29)
    r = NextMonth.get_nextmonthdate(date(2023,12,29))
    assert r == date(2024,1,29)
    r = NextMonth.get_nextmonth15(date(2023,12,29))
    assert r == date(2024,1,15)
    r = NextMonth.get_nextmonth15(date(2023,10,25))
    assert r == date(2023,11,15)

    r = NextMonth.get_next15(date(2023,10,5))
    assert r == date(2023,10,15)
    r = NextMonth.get_next15(date(2023,10,14))
    assert r == date(2023,10,15)
    r = NextMonth.get_next15(date(2023,10,15))
    assert r == date(2023,11,15)
    r = NextMonth.get_next15(date(2023,11,15))
    assert r == date(2023,12,15)
    r = NextMonth.get_next15(date(2023,12,15))
    assert r == date(2024,1,15)
    r = NextMonth.get_next15(date(2023,12,21))
    assert r == date(2024,1,15)

    r = NextMonth._retreat_month(date(2023,3,31), 31)
    assert r == date(2023,2,28)
    r = NextMonth._retreat_month(date(2024,3,31), 31)
    assert r == date(2024,2,29)
    r = NextMonth._retreat_month(date(2023,5,15), 0)
    assert r == date(2023,4,1)

    r = NextMonth._advance_month(date(2023,1,31), 31)
    assert r == date(2023,2,28)
    r = NextMonth._advance_month(date(2024,1,31), 31)
    assert r == date(2024,2,29)
    r = NextMonth._advance_month(date(2023,5,15), 0)
    assert r == date(2023,6,1)

class NextMonth:
    ''' class solution '''
    TOTAL_GB = 29

    def __init__(self, td=None):
        self.today = td if td else get_today()

    def __str__(self):
        return f'today: {self.today}'

    @staticmethod
    def _advance_month(d: date, day: int) -> date:
        '''
        Return a date in the next month using `day`.

        The requested day is clamped to the valid range of the next
        month, so this function always returns a valid date.
        '''
        target_year = d.year + (1 if d.month == 12 else 0)
        target_month = 1 if d.month == 12 else d.month + 1

        if target_year > date.max.year:
            return date.max

        after_year = target_year + (1 if target_month == 12 else 0)
        after_month = 1 if target_month == 12 else target_month + 1
        if after_year > date.max.year:
            target_last = date.max
        else:
            first_after = date(after_year, after_month, 1)
            target_last = first_after - timedelta(days=1)

        clamped_day = max(1, min(day, target_last.day))
        return target_last.replace(day=clamped_day)

    @staticmethod
    def _retreat_month(d: date, day: int) -> date:
        '''
        Return a date in the previous month using `day`.

        The requested day is clamped to the valid range of the previous
        month, so this function always returns a valid date.
        '''
        first_of_month = d.replace(day=1)
        try:
            prev_month_last = first_of_month - timedelta(days=1)
        except OverflowError:
            return date.min

        clamped_day = max(1, min(day, prev_month_last.day))
        return prev_month_last.replace(day=clamped_day)

    @staticmethod
    def get_nextmonthdate(x: date) -> date:
        ''' https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime '''
        return NextMonth._advance_month(x, x.day)

    @staticmethod
    def get_nextmonth15(d: date) -> date:
        ''' get next month 15 '''
        return NextMonth._advance_month(d, 15)

    @staticmethod
    def get_next15(d: date) -> date:
        ''' get next 15 '''
        if d.day >= 15:
            return NextMonth._advance_month(d, 15)
        return d.replace(day=15)

    @staticmethod
    def get_prev16(d: date) -> date:
        ''' get prev 16 '''
        if d.day > 16:
            return d.replace(day=16)
        if d.day == 16:
            return d
        return NextMonth._retreat_month(d, 16)

    @staticmethod
    def get_this15(d: date) -> date:
        ''' get 15 this month '''
        return d.replace(day=15)

    def action(self):
            ''' action '''
            p = NextMonth.get_prev16(self.today)
            n = NextMonth.get_next15(self.today)
            print(f"between: {p}, {n}")
            assert n > p
            ratio = (n - self.today) / (n - p)
            mass = self.TOTAL_GB * ratio
            prt(f'at least > {ratio*100:.0f}%,\nleast: {mass:.2f} GB / {self.TOTAL_GB} GB')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        print(obj)
        obj.action()

def main():
    ''' main '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--self-test',
        action='store_true',
        help='run internal date assertions and report result',
    )
    args = parser.parse_args()

    if args.self_test:
        try:
            test_dates()
        except AssertionError:
            print('self-test: FAIL')
            print(traceback.format_exc().strip())
            return 1
        print('self-test: PASS')
        return 0

    NextMonth.run()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
