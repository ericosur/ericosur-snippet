#!/usr/bin/python

# reference: http://blog.linux.org.tw/~jserv/archives/002004.html
# reference: http://www.mste.uiuc.edu/reese/buffon/

import random, math

def throw_needle():
	max_try = 99991
	crossing = 0

	for i in xrange(max_try):
		theta = math.pi * random.random()	# 0 <= theta < pi
		x = random.random()	# 0 <= x < 1
		if x <= 0.5 * math.sin(theta):	# crossing
			crossing += 1

	est_pi = float(max_try) / float(crossing)
	err = abs(est_pi - math.pi) / math.pi * 100
	print "try %d and crossing %d, pi = %.6f, err rate = %.4f" % (max_try, crossing, est_pi, err)
	return (err, est_pi)	# return a tuple for err and pi

def main():
	repeat = 100
	result = {}
	for i in xrange(repeat):
		t = throw_needle()
		result[ t[0] ] = t[1]	# store returned tuple to dict

	print "after %d repeat, the nearest pi = %.6f, err%% = %.4f" % ( repeat, result[ min(result) ], min(result) )
	print "after %d repeat, the farest pi = %.6f, max err%% = %.4f" % ( repeat, result[ max(result) ], max(result) )

if __name__ == '__main__':
	main()
