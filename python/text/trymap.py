#!/usr/bin/python

from string import upper, join, split

def flip(s):
	a = list(s)
	a.reverse()
	return join(a,'')

def capize(s):
	a = split(s, ' ')
	def mycap(s):
		sl = list(s)
		sl[0] = upper(sl[0])
		return join(sl,'')
	a = map(mycap, a)
	#print a
	return join(a,' ')

normalize = lambda s: join(split(s), ' ')

s = '''once upon a time,
there was a castle in
the bad land'''

print flip(s)
print capize(normalize(s))
