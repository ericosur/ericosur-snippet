def test_even_divide(nn):
	for i in xrange(1,20):
		if nn % i != 0:
			return 0
	return 1

def call_func(nn):
	if test_even_divide(nn):
		print(nn,"is evenly divided")
	else:
		print(nn,"cannot evenly divided")

if __name__ == '__main__':
	call_func(232792560)
	call_func(939064810)

