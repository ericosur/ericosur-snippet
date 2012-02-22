'''
http://projecteuler.net/problem=4
http://en.wikipedia.org/wiki/Palindromic_number
http://www.csie.ntnu.edu.tw/~u91029/Palindrome.html

'''

def palindrome(n):
	'''
	to test n is palindrome or not, return 1 or 0
	'''
	s = list(n)
	for i in xrange(len(s)):
		if s[i] != s[len(s)-1-i]:
			return 0
	return 1



if __name__ == '__main__':
	result = []
	mymax = 1
	cnt = 0
	for m in xrange(999,800,-1):
		for n in xrange(999,800,-1):
			cnt += 1
			multi = m * n
			if multi < mymax:
				break
			if palindrome(str(multi)):
				result.append(multi)
				if multi > mymax:
					mymax = multi
					print(multi,"=",m,"x",n)
					break

	print("after test",cnt,"numbers to get max palindrome")
	print("my max", mymax)
	print("max palindrome is",max(result))
