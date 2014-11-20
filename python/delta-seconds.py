import datetime

birthday = datetime.datetime(2012,02,10,16,44)
base = 2

for i in xrange(2,30):
	print i, ": ", birthday + datetime.timedelta(seconds = base**i)

