import cPickle

cond = True
while cond:
	if __name__ == '__main__':
		cond = False
		data_file = 'snowball.p'
		snow_dict = {}
		cnt = 0
		miss_list = []

		try:
			inf = open(data_file, 'r')
			snow_dict = cPickle.load(inf)
			inf.close()
		except IOError:
			print "cannot load"
			break

		print 'beg: len',len(snow_dict)
		#print snow_dict.keys()

		for kk in snow_dict.keys():
			for vv in snow_dict[kk]:
				cnt += 1
				if not (vv in snow_dict):
					snow_dict[vv] = snow_dict[kk][snow_dict[kk].index(vv):]

		print 'cnt', cnt
		print 'end: len',len(snow_dict)
		result = snow_dict.keys()
		result.sort()
		#print result

		# store into pickle file
		ouf = open(data_file, 'w')
		cPickle.dump(snow_dict, ouf)
		ouf.close()
