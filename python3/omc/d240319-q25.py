#!/usr/bin/env python3
# coding: utf-8

'''
Q25. 一個正整數，如果從左往右和從右往左的數位排列順序一樣，我們稱它為回文數,
例如232，4774，6都是回文數。已知一個六位回文數能被75整除，且得到的商也是回文數,
試求這個商

'''

from utils import A002113_list


def digit_sum(n):
    ''' given number n, return sum of digits
    n = 1234, return 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    return sum(ns)


def main():
    ''' main '''
    the_list = A002113_list(1_000_000)
    print(len(the_list))
    for x in the_list:
        if 100000 < x:
            if x % 75 == 0:
                print(x, x//75)

if __name__ == '__main__':
    main()
