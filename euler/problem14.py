#!/usr/bin/python
'''
http://projecteuler.net/problem=14
'''
import cPickle

def snow_number_seq(n):
	'''
	original method to calculate snow number by loop
	'''
	seq = []
	cnt = 0
	while n > 1:
		cnt += 1
		if n & 1:	# n is odd
			n = 3 * n + 1
		else:
			n = n / 2
		seq.append(n)
	return seq

def snowball(n):
	'''
	recursive method to calculate snow number, and
	it will save the calculated sequence
	'''
	global snow_dict
	global snow
	global cnt
	global not_included_cnt

	cnt += 1
	if cnt > 1e4:
		print "to many recursive and stop..."
		return

	if (n != 1) and (n in snow_dict):
		snow.extend(snow_dict[n])
		return

	snow.append(n)

	if not (n in snow_dict):
		not_included_cnt += 1

	if n <= 1:
		return
	elif n & 1:	# n is odd
		#print 'o',
		snowball(3*n+1)
	else:
		#print 'o',
		snowball(n/2)



if __name__ == '__main__':
	data_file = 'snowball.p'
	snow_dict = {1:[1], 2:[2, 1]}
	storage = 1
	cnt = 0
	# it takes long time if upperlimit is large
	upperlimit = 1000000
	i = int(upperlimit/2)
	not_included_cnt = 0

	print 'upperlimit:', upperlimit

	if storage:
		try:
			inf = open(data_file, 'r')
			snow_dict = cPickle.load(inf)
			inf.close()
		except IOError:
			# init values
			snow_dict = {1:[1], 2:[2, 1]}

	maxlen = 0
	maxidx = 0
	while i < upperlimit:
		i+=1
		snow = []
		cnt = 0
		snowball(i)
		if len(snow) > maxlen:
			maxlen = len(snow)
			maxidx = i

		#print i,'cnt', cnt,'len', len(snow) #,'snow', snow
		if not i in snow_dict:
			snow_dict[i] = snow

	#print 'snow_dict key', snow_dict.keys()
	print 'not_included_cnt', not_included_cnt
	print 'max len is', maxlen, 'max idx: ', maxidx;

	# store into pickle file
	if storage:
		ouf = open(data_file, 'w')
		cPickle.dump(snow_dict, ouf)
		ouf.close()

'''
if __name__ == '__main__':
	maxlen = 0
	maxidx = 0
	upperlimit = 30
	#i = int(upperlimit/2)
	i=0
	longest_seq = []
	verbose = 1
	while i < upperlimit:
		i += 1
		reseq = snow_number_seq(i)
		if verbose:
			print i,':',reseq
		if len(reseq) > maxlen:
			maxlen = len(reseq)
			maxidx = i
			longest_seq = reseq
	print 'maxlen:',maxlen,"max:",maxidx
	print "longest_seq", longest_seq
'''