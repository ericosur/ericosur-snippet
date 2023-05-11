#!/usr/bin/env python3
# coding: utf-8

'''
a large number n = 191919....19
what is a mod 99 ?
'''

import math

def main():
    ''' main '''
    tok = '19'
    res = ''
    for _ in range(20):
        res = res + tok
    print('len:', len(res))
    big_value = int(res)
    r1 = big_value % 99
    print('log10:', math.log10(big_value))
    r2 = (19 * 20) % 99
    print(f'r1:{r1}, r2:{r2}')


if __name__ == '__main__':
    main()
