#!/usr/bin/python

from datetime import timedelta, datetime
import time

# get current time
foo = datetime.fromtimestamp(time.time())
foo = foo.replace(microsecond=0)  # remove microsecond part
print foo;

# define offset 1 day
offset = timedelta(days=1)
print offset

# get yesterday
foo -= offset
print foo
