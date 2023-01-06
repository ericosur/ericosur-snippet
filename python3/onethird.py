#!/usr/bin/python
# coding: utf-8

def is_four_digit(n):
	if 1000 <= n <= 9999:
		return True
	return False

def is_five_digit(n):
	if 10000 <= n <= 99999:
		return True
	return False

def check_nine_digit(m, n):
	origin = '123456789'
	digits = list(origin)
	#print(digits)
	if is_four_digit(m) and is_five_digit(n):
		#print(list(str(m)), list(str(n)))
		t = []
		t.extend(list(str(m)))
		t.extend(list(str(n)))
		#print(t)
		for i in t:
			if i == '0':
				return False
			try:
				digits.remove(i)
			except ValueError:
				#print(f'element not found: {i}')
				return False
			if len(digits) == 0:
				return True
	else:
		#print(f"invalid input: {m} or {n}")
		return False

	return False

def test():
	assert(is_four_digit(999)==False)
	assert(is_four_digit(1000))
	assert(is_four_digit(9999))
	assert(is_four_digit(10000)==False)

	assert(is_five_digit(999)==False)
	assert(is_five_digit(1000)==False)
	assert(is_five_digit(9999)==False)
	assert(is_five_digit(10000))
	assert(is_five_digit(99999))
	assert(is_five_digit(100000)==False)

def test2():
	assert(check_nine_digit(1, 2)==False)
	assert(check_nine_digit(1000, 2000)==False)
	assert(check_nine_digit(1000, 20000)==False)
	assert(check_nine_digit(10000, 2000)==False)
	assert(check_nine_digit(1234, 56789))
	assert(check_nine_digit(9876, 54321))

	assert(check_nine_digit(9076, 54321)==False)
	assert(check_nine_digit(5823, 17469))


def try_and_error():
	for upper in range(1000, 10000):
		lower = upper * 3
		if check_nine_digit(upper, lower):
			print(f'{upper} / {lower}')


def main():
	''' main '''
	#test2()
	try_and_error()

if __name__ == '__main__':
	main()
