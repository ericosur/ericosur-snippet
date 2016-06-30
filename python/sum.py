#!/usr/bin/env python

# just a trivia script to use foo-loop and print

t = 0
max_size = 100

# sum from 0 to 100
for i in xrange(max_size + 1):
	t += i;

print("sum from 1 to %d: %d" % (max_size, t))

