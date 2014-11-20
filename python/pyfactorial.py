#!/usr/bin/env python

'''
a very trival script to show how to use sympy.factorint()
to factorize an integer (or determine a prime?)

needed module: sympy
'''

from sympy import factorint

while 1:	# input value <= zero to exit
	val = input("input an postive integer (0 to quit): ")
	if val <= 0: break
	fdict = factorint(val)
	print fdict

