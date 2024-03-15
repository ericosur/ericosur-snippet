#!/usr/bin/python3
# coding: utf-8

'''
P28 Q14 有一種四位數滿足以下條件，用這個數減去它各位數字之和的10倍，
得到的差等於3015，這樣的四位數中最大的那個是多少？
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
    for n in range(10000,1000,-1):
        ds = digit_sum(n)
        r = n - ds * 10
        if r == 3015:
            print(n, ds)z

if __name__ == '__main__':
    main()
