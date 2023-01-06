#!/usr/bin/python3
# coding: utf-8

'''
a, b, c, d are four different digits,
and abc + ab = b = ddd
'''

def test():
	''' run '''
	assert Solution.has_duplicate(0) is False
	assert Solution.has_duplicate(10) is False
	assert Solution.has_duplicate(22) is True
	assert Solution.has_duplicate(98) is False
	assert Solution.has_duplicate(100) is True
	assert Solution.has_duplicate(111) is True
	assert Solution.has_duplicate(123) is False


class Solution():
	def __init__(self, v):
		self.input = v
		dig = list(str(v))
		self.a = int(dig[0])
		self.b = int(dig[1])
		self.c = int(dig[2])
		self.d = 0

	@staticmethod
	def has_duplicate(v):
		digits = set(str(v))
		return len(digits) != len(str(v))

	def check(self):
		m1 = self.a * 100 + self.b * 10 + self.c * 1
		m2 = self.a * 10 + self.b * 1
		m3 = self.b
		tmp = m1 + m2 + m3
		if tmp % 111 == 0:
			#print(f'{m1} + {m2} + {m3}')
			#print(f'input: {self.input} tmp: {tmp}')
			return True
		return False

	@staticmethod
	def report(v):
		m1 = v
		m2 = v // 10
		m3 = m2 % 10
		m4 = m1 + m2 + m3
		print(f'{m1} + {m2} + {m3} = {m4}')
		print()


def run():
	cnt = 0
	for i in range(100,1000):
		if Solution.has_duplicate(i):
			#print(f'reject {i}')
			continue
		if i < 100:
			continue
		sol = Solution(i)
		if sol.check():
			sol.report(i)

		cnt += 1
	#print(f'cnt: {cnt}')

def main():
	''' main '''
	run()

if __name__ == '__main__':
	main()
