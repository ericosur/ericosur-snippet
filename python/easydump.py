#!/usr/bin/python

# easy dump

# not pass under python 3.0

import sys

if len(sys.argv) > 1:
	fname = sys.argv[1]
	print("process %s" % fname)
else:
	print("no file name is specified")
	sys.exit()

cnt = 0
for line in open(fname, 'rb').read():
	cnt += 1
	#print('%02x' % ord(line), end=' ')
	print '%02x ' % ord(line)
	if (cnt != 0) and not (cnt % 16):
		print()
