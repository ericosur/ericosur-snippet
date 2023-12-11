#!/usr/bin/env python
# coding: utf-8

'''
Monte Carlo method to calculate pi
from comments of:
http://programmingpraxis.com/2009/10/09/calculating-pi/2/
'''

import timeit
from random import random


def get_pi(n):
    ''' get approx pi, n is number of repeat '''
    return 4*float(sum(1 if (random()**2 + random()**2) <= 1 else 0 for i in range(n)))/n

def main():
    ''' main '''
    print('start...')
    start = timeit.default_timer()
    print("approx pi =", get_pi(10**8))
    end = timeit.default_timer()
    print('duration: ', (end - start))

if __name__ == '__main__':
    main()
