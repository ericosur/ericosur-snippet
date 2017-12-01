#!/usr/bin/python

from datetime import timedelta, datetime
import time

# get current time
foo = datetime.fromtimestamp(time.time())
foo = foo.replace(microsecond=0)  # remove microsecond part
print("current time from time stamp: {0}".format(foo))

# define offset 1 day
offset = timedelta(days=1)
print("timedelta: {0}".format(offset))

# get yesterday
foo -= offset
print('current - timedelta = "{0}"'.format(foo))
