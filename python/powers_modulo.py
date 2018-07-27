#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
try to calculate p ** q mod n

it is used by last-digit-power.py

'''

def _powmod(p, q, n):
	'''
		驗證答案是否正確
	'''
	return p ** q % n


def powmod(p, q, n):
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
		cc = _powmod(p, q, n)
		dd = powmod(p, q, n)
		print("%d ** %d %% %d = %d" % (p, q, n, dd))
		if cc != dd:
			print("error!!!")

if __name__ == '__main__':
	test(99)
