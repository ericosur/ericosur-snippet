#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo datetime:
yesterday = today - timedelta
'''

from __future__ import print_function

import time
from datetime import datetime, timedelta


def main():
    '''main function'''
    # get current time
    today = datetime.fromtimestamp(time.time())
    today = today.replace(microsecond=0)  # remove microsecond part
    print(f"current time from time stamp: {today}")

    # define offset 1 day
    offset = timedelta(days=1)
    print(f"timedelta: {offset}")

    # get yesterday
    today -= offset
    print(f'current - timedelta = "{today}"')

if __name__ == '__main__':
    main()
