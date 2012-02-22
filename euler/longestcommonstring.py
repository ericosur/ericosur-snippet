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

if __name__ == '__main__':
	s = '12345678123456789'
	print s[len(s)/2:]
	lcs = LongestCommonSubstring(s, s[len(s)/2:])
	print lcs
	if lcs == s[len(s)/2:] and s.find(lcs) == 0:
		print 'fuck'
	else:
		print 'shit'

