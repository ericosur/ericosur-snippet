#!/usr/bin/env python
'''
reference from http://www.cg45.cn/archives/246
to find P, which satisfy:
	P = m ** 2 + n ** 2
	P is a prime and P < 10000
	m and n are primes as well
'''

def isPrime(nn):
	'''
		a wrapper function of miller_rabin()
	'''
	from MillerRabin import miller_rabin
	return miller_rabin(nn)

def test():
	'''
		m, n, P are primes, 
		only n = 2 would make P odd because m and m*m are odd
	'''
	import math
	N = 10000
	cnt = 0
	for m in xrange( 3, int(math.sqrt(N)), 2 ):
		if isPrime(m):
			if isPrime( m**2 + 4):
				print "%d = %d ** 2 + 2 ** 2" % ( (m**2 + 4), m )
				cnt += 1
	
	return cnt

'''
main()
'''
result = test()
print "result: ", result

