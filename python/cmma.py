#!/usr/bin/python

# a stupid python script add ``'`` around every characters
# for example, "hello" would be
# 'h', 'e', 'l', 'l', 'o'
#

str = "the quick smart fox jumps over the lazy dog"

for ch in str:
	#print('\'', ch, '\'', ',', end=' ')
	print('\'', ch, '\'', ',',)

print()

for ch in str:
	#print("\'%c\', " % ch, end=' ')
	print("\'%c\', " % ch,)
