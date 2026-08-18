#!/usr/bin/env python3

'''
profiling a slow function
'''

import argparse
from time import perf_counter as pc
from time import sleep, time
from timeit import default_timer

from madlog import get_logd, get_prt
from myutil import do_nothing

prt = get_prt()
logd = get_logd()


def mysleep(sleep_time: float) -> None:
    ''' sleep for specified time '''
    logd(f'mysleep: sleep: {sleep_time} sec')
    sleep(sleep_time)

def use_timer(func, sleep_time) -> float:
    ''' use default timer '''
    start = default_timer()
    func(sleep_time)
    during = default_timer() - start
    return during

def use_time(func, sleep_time) -> float:
    ''' using time '''
    start_time = time()
    func(sleep_time)
    duration = time() - start_time
    return duration

def use_high_performance(func, sleep_time) -> float:
    ''' using perf_counter '''
    start_time = pc()
    func(sleep_time)
    duration = pc() - start_time
    return duration

def sep(c: str) -> None:
    ''' print sep '''
    prt(c * 60)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='Profile a slow function with different timer methods')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug logging')
    parser.add_argument('-t', '--sleep-time', type=float, default=0.5, help='sleep time in seconds (default: 0.5)')
    args = parser.parse_args()
    
    global logd  # pylint: disable=global-statement
    if args.debug:
        logd = get_logd()
    else:
        logd = do_nothing
    
    def run(func, method, sleep_time):
        d = func(method, sleep_time)
        prt(f'duration of {func.__name__:20s}: {d*1000:.10f}')

    for _ in range(4):
        run(use_time, mysleep, args.sleep_time)
        run(use_timer, mysleep, args.sleep_time)
        run(use_high_performance, mysleep, args.sleep_time)

if __name__ == '__main__':
    main()
