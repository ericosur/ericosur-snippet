#!/usr/bin/python

# line break if one line is longer than IDENT

from textwrap import wrap
import re

IDENT = 99

file = open('MessageHook.hpp', 'r')
p = re.compile('\s*//')

while 1:
	line = file.readline()       # Read line by line.
	if not line:
		break

	m = p.match(line)
	if m is None:
		wrap_line = wrap(line, IDENT)
		for i in wrap_line:
			print i
	else:
		print line,

#
# the fastest way to scan the whole text file
#
#for line in open('test.txt').readlines(  ): print line
#for line in open('test.txt').xreadlines(  ):print line
#for line in open('test.txt'):                print line
#		wrap_line = wrap(line, 80)
#		for i in wrap_line:	print i
#print line
