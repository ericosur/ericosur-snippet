#!/usr/bin/python

'''
try types
'''
from types import *

def foo(x):
	if type(x) is FloatType: print "float", x
	elif type(x) is IntType: print "int", x
	elif type(x) is LongType: print "long", x

arr = [3.14159, 3982, 4397913753];
map(foo, arr)
