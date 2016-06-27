#!/usr/bin/env python

import csv
import random

def getTenNumbers():
	ten = 10
	arr = []
	for i in xrange(ten):
		arr.append(random.randint(0, 99))
	return arr

with open('eggs.csv', 'wb') as csvfile:
	sw = csv.writer(csvfile, delimiter=',',
					quotechar='"', quoting=csv.QUOTE_ALL)
	sw.writerow(getTenNumbers())
