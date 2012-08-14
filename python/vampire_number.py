#!/usr/bin/env python

'''
to find four-digit vampire numbers

http://en.wikipedia.org/wiki/Vampire_number
'''

from itertools import permutations

def find_vampire(num):
	nl = list(str(num))
	if len(nl) % 2 != 0:
		print("length is not even!")
		return

	jj = permutations(nl, 4)
	for cc in jj:
		n1 = int(cc[0] + cc[1])
		n2 = int(cc[2] + cc[3])
		if n1 * n2 == num:
			print(str(num) + " is a vampire number! " + str(n1) + " x " + str(n2))

if __name__ == '__main__':
	for val in range(1000, 9999):
		find_vampire(val)
