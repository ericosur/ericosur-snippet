#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
demo yesterday
'''

from __future__ import print_function
from datetime import timedelta, datetime
import time

def main():
    '''main function'''
    # get current time
    today = datetime.fromtimestamp(time.time())
    today = today.replace(microsecond=0)  # remove microsecond part
    print("current time from time stamp: {0}".format(today))

    # define offset 1 day
    offset = timedelta(days=1)
    print("timedelta: {0}".format(offset))

    # get yesterday
    today -= offset
    print('current - timedelta = "{0}"'.format(today))

if __name__ == '__main__':
    main()
