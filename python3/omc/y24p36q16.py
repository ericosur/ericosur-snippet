#!/usr/bin/python3
# coding: utf-8

'''
P29 Q23. 有一些四位數至少有一個數字是4但不能被4整除，求滿足這種條件的四位數的個數
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
    total = 0
    for i in range(1, 9999+1):
        total += digit_sum(i)
    print(total)

if __name__ == '__main__':
    main()
