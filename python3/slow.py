#!/usr/bin/env python3
# coding: utf-8

'''
profiling a slow function
'''

from time import time
from time import perf_counter as pc
from time import sleep
from random import randint

class JustData():
    ''' put const here '''
    upper = 4286420
    lower = 9997
    arr_size = 100


def slow():
    ''' slow function '''
    #a = [x for x in range(JustData.lower, JustData.upper +1)]
    a = list(range(JustData.lower, JustData.upper +1))
    for _ in range(JustData.arr_size):
        v = randint(JustData.lower, JustData.upper)
        if v in a:
            return True
    return False

def mysleep():
    ''' sleep 500 ms '''
    sleep(0.5)
    return 0

def basic(func=slow):
    ''' using time '''
    start_time = time()
    func()
    duration = time() - start_time
    return duration

def high_performance(func=slow):
    ''' using perf_counter '''
    start_time = pc()
    func()
    duration = pc() - start_time
    return duration

def main():
    ''' main '''
    def run(func, method):
        d = func(method)
        print('duration of {:20s}: {:.10f}'.format(func.__name__, d*1000))

    run(basic, slow)
    print('-' * 50)
    run(high_performance, slow)
    print('=' * 50)
    run(basic, mysleep)
    print('-' * 50)
    run(high_performance, mysleep)

if __name__ == '__main__':
    main()
