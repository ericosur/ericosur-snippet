'''
P29 Q24. 求最小的整數n, 使得 20182018 … 20182018985 (有n個2018) 這個數是11的倍數
'''

def evens(n):
	return (8+8*n)

def odds(n):
	return (14+3*n)

def validate(n):
	e = evens(n)
	o = odds(n)
	print(f'{n}: {e=}  {o=}')
	if abs(e-o) % 11 == 0:
		print(n)
		return True
	return False

def main():
	''' main '''
	for n in range(1,1000):
		if validate(n):
			break

if __name__ == '__main__':
	main()