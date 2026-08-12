#!/usr/bin/env python3

'''use module calendar to show calendar of this year'''

import calendar
from datetime import datetime, timedelta


def main():
    '''
    print calendar of 3 months including current month
    '''
    td = datetime.now().astimezone()

    TOTAL_MONTH = 3
    between_days = timedelta(days=30)
    for _ in range(TOTAL_MONTH):
        calendar.prmonth(td.year, td.month)
        td += between_days
        #print('td.month:', td.month)


if __name__ == '__main__':
    main()
