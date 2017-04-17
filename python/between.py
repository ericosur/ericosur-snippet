#!/usr/bin/env python
#
import datetime

#ww = [8, 30]
ww = [9, 39]
# here is time I enter workspace
from_time = datetime.datetime.now().replace(hour=ww[0],minute=ww[1],second=0,microsecond=0)
print from_time

# current time
now_time = datetime.datetime.now().replace(microsecond=0)
print now_time

# need more than work_hour
work_hour = datetime.timedelta(hours=9)


if now_time - from_time > work_hour:
    print "ok, long enough"
else:
    print "nok, should be:", from_time + work_hour
