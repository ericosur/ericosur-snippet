#!/usr/bin/python
'''
use cPickle to load fib.p
'''
import cPickle

fname = 'fib.p'

inf = open(fname, "r")
mydata = cPickle.load(inf)
inf.close()

print("there are %d entries in %s" % (len(mydata), fname))
