#!/usr/bin/python

def mydiv(d):
	m = 1
	r = 1
	cnt = 0
	limit = d * 10
	flag = 0
	seq = ''
	while True:
		if cnt > limit:
			break
		if len(seq) >= (d - 1)*2:
			break
		while (m < d):
			if flag != 0:
				seq = seq + '0'	# seq.append(0)
			m = m * 10
			flag = 1
			cnt += 1
		flag =0
		r = m % d
		q = int(m / d)
		cnt += 1
		seq = seq + str(q) # seq.append(q)
		m = r
		if m == 0:
			break

	return seq

def read_primes():
	import re
	p = re.compile('\d+')
	primes = []
	cnt = 0
	fname = 'basic_prime.txt'
	for line in open(fname, 'r').readlines():
		m = p.match(line)
		if m is None:
			cnt += 1
		else:
			primes.append(int(m.group()))
	return primes

'''
def LongestCommonSubstring(S1, S2):
	M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
	longest, x_longest = 0, 0
	for x in xrange(1,1+len(S1)):
	    for y in xrange(1,1+len(S2)):
	        if S1[x-1] == S2[y-1]:
	            M[x][y] = M[x-1][y-1] + 1
	            if M[x][y]>longest:
	                longest = M[x][y]
	                x_longest  = x
	        else:
	            M[x][y] = 0
	return S1[x_longest-longest: x_longest]
'''
'''
def CheckRepeatString(s, n):
	s = mydiv(n)
	#print s, len(s)
	#print "half: " + s[len(s)/2:]
	lcs = LongestCommonSubstring(s, s[len(s)/2:])
	#print 'lcs: ' + lcs
	if lcs == s[len(s)/2:] and s.find(lcs) == 0:
		print 'ok: len: ' + str(len(lcs))
	else:
		print 'shit'
'''

def SumString(s):
	sum = 0
	for sub in s:
		#print 'sub: ' + sub,
		sum += int(sub)
		#print 'sum: ' + str(sum)
	return sum


def CheckNines(s):
	'''
	s = '0010030090270812437311935807422266800401203610832497492477432296890672016048144433299899699097291875626880641925777331995987963891675025075225677031093279839518555667'
	'''
	#print 'CheckNines('+s+')'
	ll = len(s)
	if (ll < 1) and (ll % 2 != 0):
		#print 'fail to pass, ll: ' + str(ll)
		return False

	nine_len = len(s)/2
	sum = 0
	nine_str = ''
	i = 0
	while i < nine_len:
		nine_str = nine_str + '9'
		i += 1
	#print len(nine_str)
	#print 'nine_str: ' + nine_str
	if len(s)/2 < 1:
		return False
	pp = int(s[:len(s)/2])
	qq = int(s[len(s)/2:])
	sum = pp + qq
	#print 'sum: ' + str(sum)
	if str(sum) == nine_str:
		#print 'true!'
		return True
	else:
		return False


if __name__ == '__main__':
	'''
	cnt = 0
	primes = read_primes()
	for p in primes:
		cnt += 1
		result = mydiv(p)
		print "##### " + str(p),
		CheckRepeatString(result, p)
		if cnt > 999:
			break
	'''
	cnt = 0
	maxlen = 1
	maxp = 2
	retl = 0
	#primes = read_primes()
	#primes = [7, 11, 13]
	for p in xrange(900,999):
		#print 'p: ' + str(p)
		cnt += 1
		if cnt > 9999:
			break
		result = mydiv(p)
		#print 'result: ' + result
		tl = 2
		while tl < len(result):
			s = result[0:tl]
			if CheckNines(s):
				print 'p: ' + str(p) + '  s: 0.(' + s + ')...'
				retl = tl
				break
			else:
				tl += 2
				retl = 0

		if retl > maxlen:
			maxlen = tl
			maxp = p

	print 'maxlen: ' + str(maxlen)
	print 'maxp: ' + str(maxp)

