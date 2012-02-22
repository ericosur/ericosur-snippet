'''
http://projecteuler.net/problem=6
'''


def sum_squre(n):
	sum = (1+100)*100/2
	answer = sum * sum;
	print "answer", answer
	return answer

def sqare_sum(n):
	i = 1
	sum = 0
	while i<=upperlimit:
		sum = sum + i*i
		i+=1
	print "sqare sum:", sum
	return sum

if __name__ == '__main__':
	upperlimit=100
	mm = sum_squre(upperlimit)
	nn = sqare_sum(upperlimit)
	print mm-nn
