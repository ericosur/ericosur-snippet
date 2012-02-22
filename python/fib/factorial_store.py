#!/usr/bin/python

import cPickle
import random

'''
to demo a step multiple function which would store calculated step_mul(n)
to elimate unnecessary recursive and calculation
'''


def step_mul(n):
	'''
	if step_mul(n) is already calculated, it would not
	re-calculate it again.
	'''
	global stepvalues

	if n <= 2:
		return 1
	elif n in stepvalues:
		print '.',
		return stepvalues[n]
	else:
		print 'c',
		stepvalues[n] = n * step_mul(n - 1)
		return stepvalues[n]


stepvalues = {}
data_file = 'stepvalues.p'

if __name__ == '__main__':
	try:
		inf = open(data_file, "r")
		stepvalues = cPickle.load(inf)
		inf.close()
	except IOError:
		stepvalues = {1:1, 2:2}	# init values

	for i in xrange(100):
		n = random.randint(10, 500)
		print "%d! = %d" % (n, step_mul(n))

	# store into pickle file
	ouf = open(data_file, "w")
	cPickle.dump(stepvalues, ouf)
	ouf.close()
