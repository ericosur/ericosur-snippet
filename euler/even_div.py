# code: utf-8


def test_even_divide(nn):
	for i in range(1, 20):
		if nn % i != 0:
			return False
	return True

def call_func(nn):
	if test_even_divide(nn):
		print(nn,"is evenly divided")
	else:
		print(nn,"cannot evenly divided")

if __name__ == '__main__':
	call_func(232792560)
	call_func(939064810)

