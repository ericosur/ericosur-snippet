#!/usr/bin/python
#
# to list black Friday
#

import datetime

FROM_YEAR = 2010
TO_YEAR = 2020
MIN_MONTH = 1
MAX_MONTH = 12
WEEKDAY_FRIDAY = 4	# 0:MON, 1:TUE, 2:WED, 3:THU, 4:FRI, 5:SAT, 6:SUN

for yr in xrange(FROM_YEAR, TO_YEAR+1):
	for mnth in xrange(MIN_MONTH, MAX_MONTH+1):
		dd = datetime.datetime(yr, mnth, 13)
		if dd.weekday() == WEEKDAY_FRIDAY:
			print dd.isoformat(), "is Black Friday"
