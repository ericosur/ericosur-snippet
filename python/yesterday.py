#!/usr/bin/python

import datetime
import time
from datetime import timedelta

foo = datetime.datetime.fromtimestamp(time.time())
print foo;

offset = timedelta(days=1)
print offset

foo -= offset
print foo
