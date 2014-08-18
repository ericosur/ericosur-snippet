#!/usr/bin/env python

'''
To know how many numbers could be elimated by these small primes as factor.
'''

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

target = range(1000, 10000)	# 1000 ... 9999
print "len(target): ", len(target)
cnt_array = []

for pp in small_primes:
	cnt = 0
	for nn in target:
		if nn % pp == 0:
			cnt += 1
			target.remove(nn)
	print "filtered by ", pp, ", count: ", cnt, "len(target): ", len(target)
	cnt_array.append(cnt);
	if len(target) < 20:
		print "target: ", target

print "end..."
print "len(target): ", len(target)
print "target: ", target

left = 9999-1000+1
sum = 0.0
for cc in cnt_array:
	sum += float(cc) / left
	print "sum: ", sum

print "cnt sum: ", sum
