#!/usr/bin/env python3
# coding: utf-8

'''
foobar
'''

import os
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "..")
sys.path.insert(0, "myutil")
from myutil import get_dow, get_doom_num, get_epoch, WhatNow
from myutil import is_windows, is_cygwin, get_platform

def show(msg):
    ''' show '''
    print(msg)

def what_now():
    '''
        what now
    '''
    now = WhatNow()
    # Extract hour and minute
    print(f'{now.year=}')   # date +%Y
    print(f'{now.month=}')  # date +%m
    print(f'{now.day=}')    # date +%d
    print(f'{now.hour=}')   # date +%H
    print(f'{now.minute=}') # date +%M

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
