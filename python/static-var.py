#!/usr/bin/env python

'''
try the python static variable and static method
http://stackoverflow.com/questions/68645/python-static-variable
'''

class MyClass:
	i = 3	# looks like a static var, but not similar as C++/Java

	@staticmethod
	def show():
		print "show(): ", MyClass.i	# static method access static var
	
	def show2(self):
		print "show2(): ", self.i	# here is a varialbe of instance

MyClass.i = 5
MyClass.show()	# show 5

m = MyClass()
m.i = 4
m.show2()	# show 4

