#!/usr/bin/python

# provice a recursive version of gcd

def gcd(m, n):
	'''
	calculate gcd number by rescursive
	'''
	if n == 0:
		return m
	else:
		return gcd(n, m % n)

if __name__ == '__main__':
	import sys
	#import locale
	import os

	if len(sys.argv) == 1:	# no arguments
		print("you may input two number by argument")
		a = 1280
		b = 1024
	else:
		try:
			a = int(sys.argv[1])
			b = int(sys.argv[2])
		except ValueError:
			print("not a numeric value")
			quit()
		except:
			print("unexpected error:", sys.exc_info()[0])
			raise

	if b != 0:
		gcd_num = gcd(a, b)
		print("gcd(%d, %d) = %d" % (a, b, gcd_num))
		print("(%d : %d) = (%d : %d)" % (a, b, a/gcd_num, b/gcd_num))
	else:
		print("cannot be zero")

