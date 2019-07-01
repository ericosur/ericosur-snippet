#!/usr/bin/env python3
# coding: utf-8

'''
coin sums
problem 31
https://projecteuler.net/problem=31
how many ways to compose 2 pound (200p)
'''

import itertools as it
import operator
from math import ceil
import timeit

def main():
    ''' main '''
    MAXNUMBER = 200
    # will not take 1p into count
    coins = [200, 100, 50, 20, 10, 5, 2]
    its = []
    for cc in coins:
        pp = list(range(ceil(MAXNUMBER/cc)))
        its.append(pp)

    count = 0
    try_count = 0
    print('count start...')
    time_start = timeit.default_timer()
    res = []
    for n in it.product(its[0], its[1], its[2], its[3], its[4], its[5], its[6]):
        try:
            try_count += 1
            ans = sum(map(operator.mul, coins, n))
            # if smaller than 200p, 1p could take care
            if ans <= MAXNUMBER:
                count += 1
                res.append(n)
        except (KeyboardInterrupt, SystemExit):
            print('try: {}, hit: {}'.format(try_count, count))
            raise
    time_end = timeit.default_timer()
    count += 7  # for 1x200p, 2x100p, 4x50p, 10x20p, 20x10p, 40x5p, 100x2p
    print('finished: try: {}, hit: {}'.format(try_count, count))
    print('takes: {} seconds'.format(time_end - time_start))

    # with open('ans31.txt', 'wt') as ofh:
    #     for rr in res:
    #         ofh.write(str(rr)+'\n')


if __name__ == '__main__':
    main()
