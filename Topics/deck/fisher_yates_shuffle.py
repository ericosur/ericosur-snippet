#!/usr/bin/python

import random

# implement fisher-yates shuffle in python

def shuffle_array(arr):
	n = len(arr)
	while (n > 1):
		k = random.randint(0, n-1)
		n = n - 1
		arr[n], arr[k] = arr[k], arr[n]

def fill_array(arr, max_size=20):
	for i in range(0,20):
		arr.append(i)

def show_array(arr):
	print(arr)

if __name__ == '__main__':
	arr = []
	fill_array(arr)
	show_array(arr)
	shuffle_array(arr)
	show_array(arr)
