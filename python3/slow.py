#!/usr/bin/env python3
# coding: utf-8

'''
profiling a slow function
'''

from time import perf_counter as pc
from time import sleep, time
from timeit import default_timer

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False
from myutil import do_nothing

prt = rprint if USE_RICH else print
DEBUG = True
if DEBUG:
    logd = logger.debug if USE_LOGGER else print
else:
    logd = do_nothing


def mysleep() -> None:
    ''' sleep 500 ms '''
    SLEEP_TIME = 0.5
    logd(f'mysleep: sleep: {SLEEP_TIME} sec')
    sleep(SLEEP_TIME)

def use_timer(func) -> float:
    ''' use default timer '''
    start = default_timer()
    func()
    during = default_timer() - start
    return during

def use_time(func) -> float:
    ''' using time '''
    start_time = time()
    func()
    duration = time() - start_time
    return duration

def use_high_performance(func) -> float:
    ''' using perf_counter '''
    start_time = pc()
    func()
    duration = pc() - start_time
    return duration

def sep(c: str) -> None:
    ''' print sep '''
    prt(c * 60)

def main():
    ''' main '''
    def run(func, method):
        d = func(method)
        prt(f'duration of {func.__name__:20s}: {d*1000:.10f}')

    for _ in range(4):
        run(use_time, mysleep)
        run(use_timer, mysleep)
        run(use_high_performance, mysleep)

if __name__ == '__main__':
    main()
