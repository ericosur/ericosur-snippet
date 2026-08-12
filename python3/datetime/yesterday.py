#!/usr/bin/env python3

'''
demo datetime, and timedelta to get yesterday's date
  * get today
  * define timedelta 1 day
  * compute yesterday = today - timedelta
'''


import time
from datetime import datetime, timedelta

from be_prepared import TAIPEI_TZ

from madlog import get_prt

prt = get_prt()


def main():
    '''main function'''
    # get current time
    today = datetime.fromtimestamp(time.time(), tz=TAIPEI_TZ)
    today = today.replace(microsecond=0)  # remove microsecond part
    prt(f"current time from time stamp: {today}")

    # define offset 1 day
    offset = timedelta(days=1)
    prt(f"timedelta: {offset}")

    # get yesterday
    today -= offset
    prt(f'current - timedelta = "{today}"')

if __name__ == '__main__':
    main()
