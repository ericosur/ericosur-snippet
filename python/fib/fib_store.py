#!/usr/bin/python

import cPickle
import random

'''
to demo a fib function which would store calculated fib(n)
to elimate unnecessary recursive and calculation
'''


def fib(n):
	'''
	if fib(n) is already calculated, it would not
	re-calculate it again.
	'''
	global fibvalues

	if n <= 2:
		return 1
	elif n in fibvalues:
		print '.',
		return fibvalues[n]
	else:
		print 'c',
		fibvalues[n] = fib(n-1) + fib(n-2)
		return fibvalues[n]

fibvalues = {}
data_file = 'fib.p'

if __name__ == '__main__':
	try:
		inf = open(data_file, "r")
		fibvalues = cPickle.load(inf)
		inf.close()
	except IOError:
		fibvalues = {1:1, 2:1}	# init values

	for i in xrange(1000):
		n = random.randint(2,500)
		print "fib(%d) = %d" % (n, fib(n))

	# store the fibvalues into pickle file
	ouf = open(data_file, "w")
	cPickle.dump(fibvalues, ouf)
	ouf.close()

