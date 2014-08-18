#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from help_wawb import find_wawb, get_all_combination

my_all = get_all_combination

def gets():
	text = ''
	while 1:
		c = sys.stdin.read(1)
		text = text + c
		if c == '\n': break
	
	return text

my_all = get_all_combination()
print "len(my_all): ", len(my_all)

def get_guess_wawb(guess, wawb):
	s = raw_input("guess and ?a ?b: ")
	print "get '%s'" % (s,)

	#guess = []
	#wawb = []
	for i in xrange(4):
		guess.append(int(s[i]))
	#guess = [s[0],s[1],s[2],s[3]]
	for i in xrange(2):
		wawb.append(int(s[4+i]))
	#wawb = [s[4],s[5]]

guess = []
wawb = []
get_guess_wawb(guess,wawb)
print "guess: ", guess
print "wawb: ", wawb
#poss = find_wawb(my_all, wawb, guess)
#print "len(poss) = ", len(poss)

