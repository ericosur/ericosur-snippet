#!/usr/bin/env python
#
# convert epoch value to date/time string
#

import time

def epoch2timestr(epoch=-1):
	# Replace time.localtime with time.gmtime for GMT time.
	if epoch == -1:
		epoch = int(time.time())
		str = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(time.time()))
	else:
		str = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))
	return [epoch, str]

if __name__ == "__main__":
	print epoch2timestr()
	print epoch2timestr(1468123201)
