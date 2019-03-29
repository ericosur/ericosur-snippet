#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
get delta seconds from specified time point
'''

from __future__ import print_function
import datetime

def main():
    '''main function'''
    birthday = datetime.datetime(2012, 2, 10, hour=16, minute=44)
    #birthday = datetime.datetime(1975, 6, 17, hour=12, minute=30)
    base = 2

    for i in range(27, 32):
        print('2 ^', i, ": ", birthday + datetime.timedelta(seconds=base**i))

if __name__ == '__main__':
    main()
