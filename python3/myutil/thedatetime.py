#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful utility functions
    that wraps time, datetime functions
'''

import time
from datetime import datetime

__VERSION__ = "2025.01.07"


def get_epoch() -> int:
    ''' return int of current time epoch
        same as ```date +%s```
    '''
    return int(time.time())


def epoch2timestr(epoch: int) -> tuple:
    ''' Replace time.localtime with time.gmtime for GMT time '''
    if epoch == -1:
        epoch = int(time.time())

    msg = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))
    return (epoch, msg)

def __what_now() -> None:
    '''
        what now
    '''
    now = datetime.now()
    # Extract hour and minute
    print(f'{now.year=}')   # date +%Y
    print(f'{now.month=}')  # date +%m
    print(f'{now.day=}')    # date +%d
    print(f'{now.hour=}')   # date +%H
    print(f'{now.minute=}') # date +%M

class WhatNow():
    ''' get part of datetime.now() '''
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self._setup()

    def _setup(self):
        ''' fill up the data members '''
        t = datetime.now()
        self.year = t.year
        self.month = t.month
        self.day = t.day
        self.hour = t.hour
        self.minute = t.minute
