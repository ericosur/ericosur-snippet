#!/usr/bin/python3
# coding: utf-8

'''
to check if a date is palindrome
'''

from datetime import date, timedelta

class TestDate():
    ''' test date is a prime '''
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(s):
        '''
        [in] s: numeric string
        return True/False if palindrome number
        '''
        chs = list(s)   # chs is list of each char of s
        lns = len(s)
        for i, cc in enumerate(chs):
            if cc != chs[lns - 1 - i]:
                return False
        return True

    @classmethod
    def run(cls):
        ''' run '''
        start_d = date(2000, 1, 1)
        end_d = date(2099, 12, 31)
        curr = start_d
        cnt = 0
        serial = 0
        while curr <= end_d:
            ds = curr.strftime('%Y%m%d')    # YYYYmmdd, ie: 20190823
            serial += 1
            if cls.is_palindrome(ds):
                print(f'{ds} is palindrome number')
                cnt += 1
        # else:
        #     print(f'{s} is NOT palindrome number')
            curr += timedelta(days=1)
        print(f'from {start_d} to {end_d}, there are {cnt}/{serial} palindrome days')

def main():
    ''' main '''
    TestDate.run()

if __name__ == '__main__':
    main()
