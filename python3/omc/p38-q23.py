#!/usr/bin/env python3
# coding: utf-8

'''
P38 Q23. 一個三位數能被它的各位數字之和整除，得到的商是 q。試求 q 的最小值
'''

from utils import digit_sum


def main():
    ''' main '''
    pivot = 1000
    for x in range(100, 999+1):
        s = digit_sum(x)
        if x % s == 0:
            q = x // s
            pivot = min(pivot, q)
            print(f'{x} / {s} = {q}')

    print(f'{pivot=}')


if __name__ == '__main__':
    main()
