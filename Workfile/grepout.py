#!/usr/bin/env python3
#coding: utf-8

'''
template script

 grep -v -i bluetooth
 grep -v bt_
 grep -v ConstraintSet
 grep -v -i nearby n3.txt > n4.txt
 grep -v -i btgatt n1.txt > n2.txt

'''

import os
import shutil

class Solution():
	''' class solution '''
	FILE='wtf.log'
	RETFILE='out.txt'
	INFILE='input.txt'
	TMPFILE='tmp.txt'
	def __init__(self):
		self.value = 0

	def action(self):
		''' action '''
		grepouts = ["bluetooth", "bt_", "constraintSet", "nearby", "btgatt"]
		shutil.copyfile(self.FILE, self.INFILE)
		for g in grepouts:
			cmd = f'/usr/bin/grep -v -i {g} {self.INFILE} > {self.TMPFILE}'
			print(cmd)
			os.system(cmd)
			shutil.copyfile(self.TMPFILE, self.INFILE)
		shutil.copyfile(self.INFILE, self.RETFILE)
		print('last result:', self.RETFILE)

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
