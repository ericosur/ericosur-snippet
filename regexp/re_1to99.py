#!/usr/bin/python

import re

test = ['1', '01', '2', '03', '5', '8', '13', '21', '34', '101']
pattern = r"^([1-9][0-9]?|)$"
p = re.compile(pattern)

for i in test:
	m = p.match(i)
	print i,"\t",
	if m is None:
		print "is not matched"
	else:
		print "is matched: ",
		print m.group(1)
