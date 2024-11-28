#!/usr/bin/env python3
# coding: utf-8

'''
Q26. 在2021到8999的自然數中，有多少個數的各位數字之和能被7整除？
'''


def digit_sum(n):
    ''' given number n, return sum of digits
    n = 1234, return 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    return sum(ns)


def main():
    ''' main '''
    sevens = {7:[], 14:[], 21:[], 28:[], 35:[], 42:[]}
    cnt = 0
    for n in range(2021,8999+1):
        r = digit_sum(n)
        if r % 7 == 0:
            sevens[r].append(n)
            cnt += 1
    print(f'{cnt=}')
    for k,v in sevens.items():
        print(f'{k}: {len(v)}')


if __name__ == '__main__':
    main()
