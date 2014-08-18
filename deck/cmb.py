#!/usr/bin/env python

'''
In the game '17 pokers', combinations could be described as 
C(17, 5). This script uses ''itertools.combinations'' to list 
all possible combination.
'''
from itertools import combinations

# a = [0, 1, 2, ..., 16]
a = range(17)

# ii = C(17, 5)
ii = combinations(a, 5)

cnt = 0
for cc in ii:
	print cc
	cnt = cnt + 1

#print "cnt = ", cnt

