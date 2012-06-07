#!/usr/bin/python

import os
import glob

print 'os.getcwd(): ', os.getcwd()

flist = glob.glob('../../root/*.pl')
for f in flist:
	print f

