#!/usr/bin/env python3
#coding: utf-8

'''
template script
'''

class Solution():
	''' class solution '''
	def __init__(self):
		self.value = 0

	def action(self):
		''' action '''
		print('action!')

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
