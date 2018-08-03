#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
get delta seconds from specified time point
'''

from __future__ import print_function
import datetime

def main():
    '''main function'''
    birthday = datetime.datetime(2012, 02, 10, 16, 44)
    base = 2

    for i in xrange(27, 32):
        print('2 ^', i, ": ", birthday + datetime.timedelta(seconds=base**i))

if __name__ == '__main__':
    main()
