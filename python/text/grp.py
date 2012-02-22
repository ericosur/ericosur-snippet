#!/usr/bin/python

'''
	first example from ''Text processing in python''
'''


def isCond(line):
	''' return true if the first char is # '''
	return line[:1]=='#'

filename = "foo.txt";
selected = filter(isCond, open(filename).readlines())

print selected
