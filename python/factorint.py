#!/usr/bin/env python
'''
using sympy.factorint to factorize integers
'''
def show(value):
	'''
	use sympy.factorint() and display in formatted form
	'''
	from sympy import factorint
	if (value <= 0):
		print("must >= 0")
		return
	myd = factorint(value)
	print value,"=",
	x = list(myd.keys())
	x.sort()
	while (1):
		key = x.pop(0)
		print key, "^", myd[key],
		if len(x) == 0:	# empty
			break
		else:
			print "*",

import sys

if len(sys.argv) == 1:
    print("usage: %s [arg1] [arg2]..." % sys.argv[0])
    quit()

for x in xrange(1, len(sys.argv)):
	if sys.argv[x]:
		try:
			value = sys.argv[x]
			show(value)
			print
		except ValueError:
			print("not a numeric value")
			quit()
		except:
			print("unexpected error:", sys.exc_info()[0])
			raise
