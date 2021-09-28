#!/usr/bin/python3
# coding: utf-8

'''
a simple and stupid fib function test

It is time/memory consuming while n is large.
It took 23.81 sec to calculate fib(40)

'''

#import random
import timeit

def fib(n):
    ''' simple recursive version to get fib '''
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def main():
    ''' main '''
    m = 40
    time_start = timeit.default_timer()
    r = fib(m)
    time_end = timeit.default_timer()
    d = time_end - time_start
    print(f'fib({m}) = {r}')
    print(f'during {d}')

if __name__ == '__main__':
    main()
