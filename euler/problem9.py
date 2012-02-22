from math import sqrt
'''
http://projecteuler.net/problem=9
'''

def square_sum(m,n):
	return m*m+n*n

def test_square(val):
	root = sqrt(val)
	if root == int(root):
		return 1
	else:
		return 0

if __name__ == '__main__':
	cnt = 0
	sqcnt = 0
	for xx in xrange(1,999):
		for yy in xrange(xx+1,999-xx):
			cnt += 1
			sqsum = square_sum(xx, yy)
			sqroot = sqrt(sqsum)
			if sqroot < yy:
				break
			if test_square(sqsum):
				sqcnt += 1
				if (xx+yy+sqroot)==1000:
					print(xx,"^2 + ",yy,"^2 = ",sqroot,"^2")
	print("cnt = ", cnt)
	print("sqcnt = ", sqcnt)
