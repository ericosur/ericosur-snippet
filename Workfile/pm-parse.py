#!/usr/bin/env python3
#coding: utf-8

'''
- to get all packages
adb shell pm list packages
- query privapp permissions
adb shell pm get-privapp-permissions
'''

import os
import re

class Solution():
	''' class solution '''
	FILE='pm.txt'
	PFILE='/tmp/__pmparse.txt'
	PRIVFILE = '/tmp/__priv.txt'
	NEWLINE = '\n'

	def __init__(self):
		self.packages = []
		self.pname = ''

	def parse_file(self):
		''' parse file '''
		with open(self.FILE, 'rt', encoding='UTF-8') as fobj:
			for ln in fobj.readlines():
				ln = ln.strip()
				m = re.match(r'^package:(.+)$', ln)
				if m:
					self.packages.append(m[1])

	def parse_pfile(self):
		''' parse permission dumped file '''
		perms = []
		with open(self.PRIVFILE, 'rt', encoding='UTF-8') as fobj:
			for ln in fobj.readlines():
				ln = ln.strip()
				ln = ln.replace('{', '')
				ln = ln.replace('}', '')
				if ln:
					perms.append(ln)

		if perms:
			print(f'{self.pname}:')
			for p in perms:
				print('\t', p)

	def query_permission(self):
		''' query permission '''
		for p in self.packages:
			cmd = f'adb shell pm get-privapp-permissions {p} > {self.PFILE}'
			#print(cmd)
			os.system(cmd)
			cmd = f"sed 's/, /\\n/g' {self.PFILE} > {self.PRIVFILE}"
			#print(cmd)
			os.system(cmd)
			self.pname = p
			self.parse_pfile()

	def action(self):
		''' action '''
		#print('action!')
		#cmd = f'adb shell pm list packages > {self.FILE}'
		#os.system(cmd)
		if os.path.exists(self.FILE):
			self.parse_file()
			self.query_permission()
		else:
			print('[FAIL] something wrong...')

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
