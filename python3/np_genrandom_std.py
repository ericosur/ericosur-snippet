#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=invalid-name
#

'''
Generate random numbers that meets standard normal distribution

Functions using numpy:
rng, random, standard_normal, mean, median, std, amax, amin

The output:
  max,   min,  mean, median, stddev,  count,  lhs,  rhs
166.62, 37.00, 100.05, 100.01, 14.97, 100000, 77.59, 122.51, 86652
144.94, 55.02, 100.03, 100.00, 14.77, 99725

The first line count is the total number generated by numpy.
The lhs is -1.5 sigma, and rhs is +1.5 sigma. The last number
of the first line is the number of elements which in the (-1.5, 1.5) sigma.
The 2nd line count is the number of elements which in the (-3, 3) sigma.

'''

import time
from typing import Any
import numpy as np
from myutil import do_nothing

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

try:
    from loguru import logger  # type: ignore[import]
    USE_LOGURU = True
except ImportError:
    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    USE_LOGURU = False

SEP_REPEAT = 70
DEBUG = False
logd :Any = None
if DEBUG:
    if USE_LOGURU:
        logd = logger.debug
    else:
        import logging
        logging.basicConfig(level=logging.DEBUG)
        logd = logging.debug
else:
    logd = do_nothing

class GenerateStdNormal():
    ''' a class to generate normal distribution data '''

    default_size = 100_000

    def __init__(self):
        self.mu = 100
        self.sigma = 15
        # np's random number generator
        self.rng = np.random.default_rng(int(time.time()))
        self.lhs, self.rhs = -1, -1

    def fill_bytes(self) -> np.ndarray[Any, Any]:
        ''' fill buffer '''
        arr = self.rng.integers(0, 256, self.default_size, dtype='uint8') # 0 .. 255
        logd(type(arr))
        return arr

    def fill_stdnorm(self) -> np.ndarray[Any, Any]:
        ''' fill buffer '''
        arr = self.mu + self.sigma * self.rng.standard_normal(size=self.default_size)
        #logd(type(arr))
        return arr

    def show(self, arr: np.ndarray[Any,Any]|list[Any], extmsg: str|None=None) -> None:
        ''' show '''
        prt(f'{np.amax(arr):.2f}, {np.amin(arr):.2f}, ', end='')
        prt(f'{np.mean(arr):.2f}, {np.median(arr):.2f}, ', end='')
        prt(f'{np.std(arr):.2f}, {len(arr)}', end='')
        if extmsg:
            prt(f', {extmsg}', end='')
            prt(f', {self.count_in_scope(arr)}')
        else:
            prt()

    def test2(self) -> None:
        ''' add2() will add 4 into all elements '''
        def add2(x: np.ndarray) -> np.ndarray:
            ''' add 4 for each input '''
            return x + 4

        for _ in range(10):
            r = add2(self.fill_stdnorm())
            self.show(r)

    def filter_arr(self, arr) -> list[Any]:
        ''' filter out beyond -n * sigma to n * sigma '''
        logd("filter_arr...")
        n = 3
        tmp = [ x for x in arr if x > self.mu - n*self.sigma ]
        r = [ x for x in tmp if x < self.mu + n*self.sigma ]
        logd(type(r))
        return r

    @staticmethod
    def header():
        ''' prt header '''
        prt('   max,   min,  mean, median, stddev,  count,  lhs,  rhs, no_in_scope')
        if USE_RICH:
            prt('[bold magenta]'+ '=' * SEP_REPEAT + '[/]')
        else:
            print('=' * SEP_REPEAT)

    def get_limts(self, r: np.ndarray) -> str:
        ''' show left--right limits
            r is numpy.ndarray
        '''
        n = 1.5
        self.lhs = r.mean() - n*r.std()
        self.rhs = r.mean() + n*r.std()
        msg = f"{self.lhs:.2f}, {self.rhs:.2f}"
        return msg

    def count_in_scope(self, r: np.ndarray[Any,Any]|list[Any]) -> int:
        ''' r is numpy.ndarray, return the number which value is in the range
        '''
        return len([x for x in r if self.lhs <= x <= self.rhs])

    def count_range_filter(self, r: np.ndarray) -> int:
        ''' r is numpy.ndarray, return the number which value is in the range
        '''
        return len(list(filter(lambda x: self.lhs <= x <= self.rhs, r)))

    def sep(self):
        ''' separator'''
        #logd('sep...')
        if USE_RICH:
            prt('[bold blue]' + '-' * SEP_REPEAT + '[/]')
        else:
            print('-' * SEP_REPEAT)

    @classmethod
    def run(cls) -> None:
        ''' run demo '''
        obj = cls()
        obj.header()
        for _ in range(7):
            r = obj.fill_stdnorm()
            rb = obj.filter_arr(r)
            msg = obj.get_limts(r)
            obj.show(r, extmsg=msg)
            obj.show(rb)
            obj.sep()

def main():
    """ main function to do test """
    GenerateStdNormal.run()

if __name__ == '__main__':
    main()
