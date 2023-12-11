#!/usr/bin/env python3
# coding: utf-8

''' to calculate days between two dates '''

from datetime import date


class Solution():
    ''' class to solve this problem '''

    @staticmethod
    def date2str(d):
        ''' date object to string '''
        return str(d)

    @staticmethod
    def str2date(s):
        ''' date string to date object
            [in] 2020-01-01
        '''
        arr = s.split('-')
        try:
            vals = [int(x) for x in arr]
        except ValueError:
            print('[ERROR] str2date: invalid string to integer')
            return None
        return date(vals[0], vals[1], vals[2])

    @staticmethod
    def get_between_dates(start, end):
        ''' get dates between
            [in] str start date 2020-01-01
            [out] str end date 2020-02-29
        '''
        start_date = Solution.str2date(start)
        end_date = Solution.str2date(end)
        between = end_date - start_date
        #print(type(between), repr(between))
        return between

    @staticmethod
    def get_today_str():
        ''' get string of today '''
        return Solution.date2str(date.today())

    @staticmethod
    def get_eoy():
        ''' return the string of the date at the end of this year
            eg: 2021-12-31
        '''
        t = date.today()
        nd = date(t.year, 12, 31)
        return str(nd)

    @staticmethod
    def get_boy():
        ''' return the string of the date at the begin of this year
            eg: 2021-01-01
        '''
        t = date.today()
        nd = date(t.year, 1, 1)
        return str(nd)

    @staticmethod
    def show_diff(m, n):
        ''' test '''
        r = Solution.get_between_dates(m, n)
        print(f'Days between {m} to {n}: {r}')

    @classmethod
    def run(cls):
        ''' run demo '''
        cls.show_diff('2020-01-01', '2020-01-02')
        print('[NOTE] 2020 is leap year')
        cls.show_diff('2020-01-01', '2020-12-31')
        print('[NOTE] 2023 is not leap year')
        cls.show_diff('2023-01-01', '2023-12-31')
        print()
        print('Days from today to end of this year...')
        cls.show_diff(cls.get_today_str(), cls.get_eoy())
        print('Days from begin of this year to today...')
        cls.show_diff(cls.get_boy(), cls.get_today_str())

        print('Days from someday to today...')
        cls.show_diff(cls.get_today_str(), '2024-01-13')

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
