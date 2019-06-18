#!/usr/bin/python3
# coding: utf-8

''' a simple and stupid fib function test '''

import random

def fib(n):
    ''' simple recursive version to get fib '''
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# it is time/memory consuming while n is large
if __name__ == '__main__':
    for i in range(10):
        m = random.randint(2, 100)
        print('fib({}) = {}'.format(m, fib(m)))
