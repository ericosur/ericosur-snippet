#!/usr/bin/python

# just pick one name from name list randomly

import random

name_list = ['alice', 'bob', 'cathy', 'david', 'eric',
	'fred', 'grace', 'helen']
size = len(name_list)

for i in range(10):
	idx = random.randint(0, size-1)	# int(random.random() * size)
	print(name_list[idx], '\t',)
