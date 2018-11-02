#!/usr/bin/python

import cPickle
import random

'''
to demo a fib function which would store calculated fib(n)
to elimate unnecessary recursive and calculation

to solve project euler problem #2:
http://projecteuler.net/problem=2

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
		#print '.',
		return fibvalues[n]
	else:
		#print 'c',
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

	# to find the fib number which is even and smaller the upper_limit
	upper_limit = 4e6
	i = 1
	even_seq = []
	while (1):
		fval = fib(i)
		if fval > upper_limit:
			break
		if not fval & 1:
			even_seq.append(fval)
			#print "fib(%d) = %d" % (i, fval)
		i += 1

	print even_seq, "and sum is", sum(even_seq)


	# store the fibvalues into pickle file
	ouf = open(data_file, "w")
	cPickle.dump(fibvalues, ouf)
	ouf.close()

