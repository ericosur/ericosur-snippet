#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
try to calculate p ** q mod n
其中 simplify() 可以參考 last-digit-power.py
'''

def powmod(p, q, n):
	'''
		驗證答案是否正確
	'''
	return p ** q % n


def simplify(p, q, n):
	v = 1
	s = q
	while s > 0:
		v *= p
		v = v % n
		s -= 1
	return v	# 得到的餘數


def test(rep):
	'''
	n: repeat time
	'''
	import random
	for i in xrange(rep):
		(p, q, n) = (random.randint(10001,99999),
				random.randint(3001,7999),
				random.randint(1001,3001))
		cc = powmod(p, q, n)
		dd = simplify(p, q, n)
		print "%d ** %d %% %d = %d" % (p, q, n, dd)
		if cc != dd:
			print "error!!!"

'''
p = 2029
q = 10
n = 17
simplify(p, q, n)
print "trad: ", powmod(p, q, n)
'''

test(99)
