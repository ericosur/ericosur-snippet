#!/usr/bin/env python

import datetime

birthday = datetime.datetime(2012,02,10,16,44)
base = 2

for i in xrange(27,32):
	print i, ": ", birthday + datetime.timedelta(seconds = base**i)

