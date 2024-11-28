#!/usr/bin/env python3
# coding: utf-8

'''
P29 Q21. 一個正整數，如果它的數位從左往右和從右往左看都是一樣的，
則稱這個數為回文數，例如 3,22, 505, 8338 都是回文數，
如果我們把全部的回文數從小到大排列，第400個回文數是多少？
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
    the_list = A002113_list(99999)
    print(len(the_list))
    print()
    print(the_list[400-1])

if __name__ == '__main__':
    main()
