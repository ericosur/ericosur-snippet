#!/usr/bin/python3
# coding: utf-8

''' to calculate days between two dates '''

from datetime import date

class Solution():
    ''' class to solve this problem '''

    @staticmethod
    def date2str(d):
        ''' date object to string '''
        return d.__str__()

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

def main():
    ''' main '''
    def test(m, n):
        ''' test '''
        r = Solution.get_between_dates(m, n)
        print('{} days'.format(r))

    test('2020-01-01', '2020-01-02')
    test('2020-01-01', '2020-12-31')
    test('2019-01-01', '2019-12-31')
    test(Solution.get_today_str(), '2020-12-31')



if __name__ == '__main__':
    main()
