#!/usr/bin/env python3

'''
foobar
'''

import os
import sys

try:
    sys.path.insert(0, ".")
    sys.path.insert(0, "..")
    sys.path.insert(0, "myutil")
    from myutil import (
        WhatNow,
        get_doom_num,
        get_dow,
        get_epoch,
        get_platform,
        is_cygwin,
        is_windows,
    )
except ImportError as e:
    print(f'ImportError: {e}')
    sys.exit(1)

def show(msg):
    ''' show '''
    print(msg)

def what_now():
    '''
        what now
    '''
    now = WhatNow()
    # Extract hour and minute
    print(f'{now.year:>4=}')   # date +%Y
    print(f'{now.month:>2=}')  # date +%m
    print(f'{now.day:>2=}')    # date +%d
    print(f'{now.hour:>2=}')   # date +%H
    print(f'{now.minute:>2=}') # date +%M

def test0():
    ''' test 0 '''
    y = 2024
    r = get_dow(y,4,1)
    print(f'dow: {r}')
    r = get_doom_num(y)
    print(f'doom num: {r}')

    r = get_epoch()
    print(f'epoch: {r}')
    os.system('date +%s')

def main():
    ''' main '''
    print(f'platform: {get_platform()}')
    if is_windows():
        print('is windows')
    if is_cygwin():
        print('is cygwin')
    what_now()

if __name__ == '__main__':
    main()
