#!/usr/bin/env python3
# coding: utf-8

'''
get some random 4 digit numbers
'''

import random


def main():
    ''' main '''
    DIVISOR = 7
    REPEAT = 10
    MIN = 1000
    MAX = 99999
    for _ in range(REPEAT):
        n = random.randint(MIN, MAX)
        (q, r) = divmod(n, DIVISOR)
        print(f'{n} / {DIVISOR} = {q}', end='')
        if r:
            print(f' ... {r}')
        else:
            print()


if __name__ == '__main__':
    main()
