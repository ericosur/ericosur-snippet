#!/usr/bin/env python3
# coding: utf-8

'''
to check if a date is palindrome
'''

from datetime import date, timedelta


def is_palindrome(the_str: str):
    ''' the shortest way to test if palindrome '''
    if not isinstance(the_str, str):
        raise ValueError
    return the_str==the_str[::-1]


def demo_palindrome():
    ''' run '''
    start_d = date(2000, 1, 1)
    end_d = date(2099, 12, 31)
    curr = start_d
    cnt = 0
    total = 0
    while curr <= end_d:
        ds = curr.strftime('%Y%m%d')    # YYYYmmdd, ie: 20190823
        total += 1
        if is_palindrome(ds):
            print(f'{ds} is palindrome number')
            cnt += 1
        curr += timedelta(days=1)
    print(f'from {start_d} to {end_d}, there are {cnt}/{total} palindrome days')

def main():
    ''' main '''
    demo_palindrome()

if __name__ == '__main__':
    main()
