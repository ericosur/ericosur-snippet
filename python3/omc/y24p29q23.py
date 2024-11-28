#!/usr/bin/env python3
# coding: utf-8

'''
P29 Q23. 有一些四位數至少有一個數字是4但不能被4整除，求滿足這種條件的四位數的個數
'''

def check_digits(n):
    ''' input n '''
    ss = list(str(n))
    if '4' in ss and n%4!=0:
        return True
    return False


def digit_sum(n):
    ''' given number n, return sum of digits
    n = 1234, return 10
    '''
    ss = list(str(n))
    ns = [ int(x) for x in ss ]
    return sum(ns)


def main():
    ''' main '''
    answers = []
    for i in range(1000, 9999+1):
        if check_digits(i):
            answers.append(i)
    print(len(answers))

if __name__ == '__main__':
    main()
