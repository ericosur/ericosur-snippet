#!/usr/bin/python3
# coding: utf-8

'''
find 11n that number root = 15
'''

import sys
import itertools as it

def get_numroot(n):
    v = [int(x) for x in list(str(n))]
    return sum(v)

def find_answer():
    for n in range(100, 1000):
        r = get_numroot(n)
        if r == 15:
            print(n)
            if n % 11 == 0:
                print("==>", n)


def main():
    ''' main '''
    print('main')
    find_answer()

if __name__ == '__main__':
    main()
