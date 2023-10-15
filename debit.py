#!/usr/bin/env python3
#coding: utf-8

'''
template script
'''

class Solution():
	''' class solution '''
	def __init__(self):
		self.value = 2400000
		self.step = 31174
		self.months = 12
		self.start_month = 11

	def action(self):
		''' action '''
		print('action!')
		_left = self.value
		_m = self.start_month
		for i in range(self.months):
			if _left <= 0:
				break
			_left = _left - self.step
			print(f'after {_m}/2: {_left}')
			_m = _m + 1
			if _m > 12:
				_m = _m - 12


	@classmethod
	def run(cls):
		''' run '''
		obj = cls()
		obj.action()

def main():
	''' main '''
	Solution.run()

if __name__ == '__main__':
	main()
