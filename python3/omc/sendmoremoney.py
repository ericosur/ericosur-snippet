#!/usr/bin/env python3
#coding: utf-8

'''
    S E N D
+   M O R E
------------
  M O N E Y
'''

from itertools import permutations

class Solution():
	''' class solution '''
	def __init__(self):
		self.letters = {}

	@staticmethod
	def is_valid(c):
		'''sendmory
		   01234567
		'''

		'''
		(s,e,n,d,m,o,r,y)=c
		tmp = int(d) + int(e)
		if tmp % 10 != int(y):
			return False
		t2 = int(n)+int(r)+tmp//10
		if t2 % 10 != int(e):
			return False
		t3 = int(e)+int(o)+t2//10
		if t3%10 != int(n):
			return False
		t4 = int(s) + int(m)+t3//10
		if t4 != int(m)*10+int(o):
			return False
		'''

		c2 = []
		for i in c:
			c2.append(int(i))
		[S,E,N,D,M,O,R,Y] = c2
		if S==0 or M==0:
			return False
		#print(S,E,N,D,"+", M,O,R,E,end=' ')
		send = S*1000+E*100+N*10+D
		more = M*1000+O*100+R*10+E
		money = M*10000+O*1000+N*100+E*10+Y
		#print(send,more,money)
		if send + more == money:
			return True
		return False

	def action(self):
		''' action '''
		msg='sendmoremoney'
		digits = list(msg)
		for d in digits:
			self.letters[d] = 1
		#print(self.letters)
		for c in permutations('0123456789',8):
			if self.is_valid(c):
				print(c)

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
