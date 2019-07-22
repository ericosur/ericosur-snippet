#!/usr/bin/python3
# coding: utf-8

'''
table: prime_100k.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

'''

import os
import sys
import pickle
import re
import random

import search_in_primes

# pylint: disable=invalid-name


def gold_bach(val):
    ''' it could be found if val < 4 * 10^17 '''
    print('test {}...'.format(val))
    with search_in_primes.StorePrime() as sp:
        if val % 2 != 0:
            print('[ERROR] must be an even number')
            return

        ret = sp.get_primes_less_than(val)
        #print(ret)
        ans = []
        for pp in ret:
            left = val - pp
            if pp > left:
                break
            if left in ret:
                ans.append((pp, left))
        print('goldbach:', ans)
        return ans


def basic_test():
    ''' basic test '''
    gold_bach(4)
    gold_bach(50)
    gold_bach(100)


def main(argv):
    if argv == []:
        _max = 1299709
        _min = 2
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 10
        # for _ in range(REPEAT):
        #     r = random.randint(_min, _max)
        #     gold_bach(r)
        #

'''
    else:
        for ss in argv:
            try:
                val = int(ss)
                test(val)
            except ValueError:
                print('{} is a ValueError'.format(ss))
                continue
'''

if __name__ == '__main__':
    main(sys.argv[1:])
