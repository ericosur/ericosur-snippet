#!/usr/bin/env python3
#coding: utf-8

'''
ratio between a month
data plan count from (mm/dd, including) prev month 16 to this month 15
get the ratio as a reference for today usage

'''

from datetime import date
HAS_CONSOLE_MODULE = False
try:
    import console
    HAS_CONSOLE_MODULE = True
except ImportError:
    print('[INFO] No console module of pythonista')

def test_dates():
    ''' test '''
    r = NextMonth.get_nextmonthdate(date(2023,2,28))
    assert r == date(2023,3,28)
    r = NextMonth.get_nextmonthdate(date(2023,1,29))
    assert r is None
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

class NextMonth():
    ''' class solution '''
    def __init__(self, td=None):
        if td:
            self.today = td
        else:
            self.today = date.today()
        td = self.today

    def __str__(self):
        msg = f'today: {self.today}'
        #msg += f'prev15: {self.prev15}, next15: {self.next15}'
        return msg

    @staticmethod
    def get_nextmonthdate(x: date):
        '''
        https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime
        '''
        try:
            nextmonthdate = x.replace(month=x.month+1)
        except ValueError:
            if x.month == 12:
                nextmonthdate = x.replace(year=x.year+1, month=1)
            else:
                # next month is too short to have "same date"
                # pick your own heuristic, or re-raise the exception:
                return None
        return nextmonthdate

    @staticmethod
    def get_nextmonth15(d: date):
        ''' get next month 15 '''
        next15 = None
        try:
            next15 = d.replace(month=d.month+1, day=15)
        except ValueError:
            if d.month == 12:
                next15 = d.replace(year=d.year+1, month=1, day=15)
            else:
                return None
        return next15

    @staticmethod
    def get_next15(d: date):
        ''' get next 15 '''
        limit = 15
        n = None
        try:
            if d.day > limit:
                n = d.replace(month=d.month+1, day=15)
            elif d.day == limit:
                n = d
            else:
                n = d.replace(day=15)
        except ValueError:
            if d.month == 12:
                n = d.replace(year=d.year+1, month=1, day=15)
            else:
                return None
        return n

    @staticmethod
    def get_prev16(d: date):
        ''' get prev 16 '''
        limit = 16
        p = None
        try:
            if d.day > limit:
                p = d.replace(day=limit)
            elif d.day == limit:
                p = d
            else:
                p = d.replace(month=d.month-1, day=limit)
        except ValueError:
            if d.month == 1:
                p = d.replace(year=d.year-1, month=12, day=limit)
            else:
                return None
        return p

    @staticmethod
    def get_this15(d: date):
        ''' get 15 this month '''
        this15 = None
        try:
            this15 = d.replace(day=15)
        except ValueError:
            return None
        return this15

    @staticmethod
    def get_ddiff(start, end):
        ''' get diff days '''
        d = end - start
        #print(f'{end} - {start} = {d}')
        return d

    def action(self):
        ''' action '''
        # duration from prev/16 to this/15
        p = NextMonth.get_prev16(self.today)
        n = NextMonth.get_next15(self.today)
        print(f"between: {p}, {n}")
        assert n>p
        nom = NextMonth.get_ddiff(self.today, n)
        denom = NextMonth.get_ddiff(p, n)
        #print(nom, denom)
        ratio = nom / denom
        mass = 24 * ratio
        msg = f'at least > {ratio*100:.0f}%,\nleast: {mass:.2f} GB'
        print(msg)
        if HAS_CONSOLE_MODULE:
            console.alert(msg)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        print(obj)
        obj.action()

def main():
    ''' main '''
    NextMonth.run()

if __name__ == '__main__':
    main()
