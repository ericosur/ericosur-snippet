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

for x in xrange(1000, 9999):
	if x:
		try:
			show(x)
			print
		except ValueError:
			print("not a numeric value")
			quit()
		except:
			print("unexpected error:", sys.exc_info()[0])
			raise

