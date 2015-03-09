#!/usr/bin/python

'''
algorithm of __Sieve of Eratosthenes__
wiki: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
and reference: http://www.csie.ntnu.edu.tw/~u91029/SieveOfEratosthenes.html

Prime Sieve of Eratosthenes
http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes
'''

import math

def fill_array(arr, arr_max):
	'''
		even numbers would not be filled in this array
	'''
	i = 3
	while i <= arr_max:
		arr.append(i)
		i += 2


def fill_array_old(arr, arr_max):
	'''
		fill array from 2 to arr_max-1
	'''
	for i in range(2, arr_max):
		arr.append(i)


def del_elem(arr, arr_max):
	global g_count
	global primes

	g_count += 1
#	print("#", g_count, arr)
#	print("prime.append(%d", arr[0])
	# the first one is prime
	primes.append(arr[0])

	pp = arr[0]
	inc = arr[0]

	while pp <= arr[-1]:
		if arr.__contains__(pp):
			arr.remove(pp)	# remove the multiples
			#print(pp, " removed")
		pp += inc;	# next multiple

	if arr[0] > math.sqrt(arr_max):
		# print("%d > %f" % (arr[0], math.sqrt(arr_max)))
		if len(arr) > 0:
			for bb in arr:
				primes.append(bb)
		return
	else:
		del_elem(arr, arr_max)

if __name__ == "__main__":
	max_number = 1000
	g_count = 0
	primes = [2]
	arr = []
	fill_array(arr, max_number)
	#print(arr)
	del_elem(arr, max_number)
	print("# total pass: %d" % g_count)
	print("# found %d primes" % len(primes))

	for pr in primes:
		print(pr)
