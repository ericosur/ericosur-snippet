#!/usr/bin/env python3

'''use module calendar to show calendar of this year'''

import calendar
from datetime import date, timedelta

'''
print calendar of month, for 3 month including this month
'''
td = date.today()

#calendar.prcal(td.year)
calendar.prmonth(td.year, td.month)
#calendar.monthrange(td.year, td.month)
TOTAL_MONTH = 2
between_days = timedelta(days=30)
count = 0
while count < TOTAL_MONTH:
    count += 1
    td += between_days
    #print(td, td.month)
    calendar.prmonth(td.year, td.month)
