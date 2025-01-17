#!/usr/bin/env python3
# coding: utf-8

'''
a simple and stupid fib function test

It is time/memory consuming while n is large.
It took 23.81 sec to calculate fib(40)

2023-05-24 Host(zen33) takes 15.14 seconds to get fib(40)
2023-05-24 Host(jeff) takes 8.91 seconds to get fib(40)

'''

from timeit import default_timer
from datetime import datetime
from socket import gethostname


def fib(n: int) -> int:
    ''' simple recursive version to get fib '''
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def prepare_msg(duration: float, ulimit: int) -> None:
    ''' prepare message '''
    dt = datetime.today().strftime('%Y-%m-%d')
    hostname = gethostname()
    msg = f'{dt} Host({hostname}) takes {duration:.3f} seconds to get fib({ulimit})'
    print(msg)

def test() -> None:
    ''' test '''
    m = 40
    print(f'calculate fib({m}) from scratch, for cached fib(), use')
    print('fib_store.py')

    time_start = default_timer()
    r = fib(m)
    time_end = default_timer()
    d = time_end - time_start
    print(f'fib({m}) = {r}, during: {d:.3f}')
    prepare_msg(d, m)

def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
