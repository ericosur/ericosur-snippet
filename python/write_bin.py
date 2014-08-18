#!/usr/bin/python

'''
demo to write a binary file
'''

'''
import binascii

hs = '5b7f887469feda'
hb = binascii.a2b_hex(hs)
'''

import random

left_size = 2 ** 30
s_size = 0
file = open("test.bin", "wb")
s = ''
while (left_size):
	left_size -= 1
	s += "%c" % random.randint(0, 0xff)
	s_size += 1
	if s_size > 16 * 1024 * 1024:
		file.write(s)
		file.flush()
		s_size = 0
		s = ''

file.close()

