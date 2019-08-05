#!/usr/bin/env python3
# coding: utf-8

'''
profiling a slow function
'''

from time import time
from time import perf_counter as pc

class JustData():
    ''' put const here '''
    upper = 4286420
    lower = 9997
    arr_size = 100


def slow():
    ''' slow function '''
    from random import randint
    a = [x for x in range(JustData.lower, JustData.upper +1)]
    for _ in range(JustData.arr_size):
        v = randint(JustData.lower, JustData.upper)
        if v in a:
            return True
    return False


def basic():
    ''' using time '''
    start_time = time()
    slow()
    duration = time() - start_time
    return duration

def high_performance():
    ''' using perf_counter '''
    start_time = pc()
    slow()
    duration = pc() - start_time
    return duration

def main():
    ''' main '''
    def run_func(func):
        d = func()
        print('duration of {:20s}: {:.20f}'.format(func.__name__, d))

    run_func(basic)
    print('-' * 40)
    run_func(high_performance)

if __name__ == '__main__':
    main()
