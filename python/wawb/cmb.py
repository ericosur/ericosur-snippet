#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations

def get_wawb(m, n):
	a = 0
	b = 0
	for i in xrange(4):
		for j in xrange(4):
			if i == j:
				if m[i] == n[j]:
					a = a + 1
			else:
				if m[i] == n[j]:
					b = b + 1

	return [a, b]


# wawb: [m, n] how many A how many B
# guess: [1,2,3,4] what the guesser guess
# returns possible list
def find_wawb(all, wawb, guess):
	cnt = 0
	possible = []
	#print "len(all): ", len(all)
	#print "wawb: ", wawb
	#print "guess: ", guess
	for elem in all:
		if wawb == get_wawb(elem, guess):
			#cnt = cnt + 1
			possible.append(elem)
			#print "possible wawb: ", elem
	#print "possible count: ", cnt
	return possible


def dump_all(all):
	cnt = 0
	zero_cnt = 0
	for elem in all_perm:
		if elem[0] == 0:
			zero_cnt = zero_cnt + 1
		print elem
		cnt = cnt + 1

	print "cnt = ", cnt
	print "zero head count = ", zero_cnt


def test_get_wawb():
	a = [1,2,3,4]
	b = [2,1,8,9]
	print get_wawb(a,b)


def test_intersection():
	p1 = find_wawb(aa, [1,2], [1,2,3,4])
	#print "p1: ", p1
	print "p1 len: ", len(p1)
	p2 = find_wawb(aa, [2,1], [2,3,4,5])
	#print "p2: ", p2
	print "p2 len: ", len(p2)

	s1 = set(p1)
	s2 = set(p2)
	print s1 & s2

def get_one_elem(allpair):
	import random

	size = len(allpair)

	idx = random.randint(0, size-1)	# int(random.random() * size)
	#print idx, all[idx]

	return allpair[idx]


# neg: 已知不可能的數字
# guess: 猜測的數字
# return: True: 沒問題，False: 數字有重複，重猜
def check_guess(neg, guess):
	if len(neg) == 0:
		return True
	for p in neg:
		for q in guess:
			if p == q:
				return False
	return True


def test_check_guess(allpair):
	neg = [1,2,3,4]
	for i in xrange(10):
		my_guess = get_one_elem(allpair)	# 隨機取一個作猜測
		print neg, " vs ", my_guess, " => ", check_guess(neg, my_guess)


def make_wawb_guess(allpair, answer):
	debug = 0
	aa = allpair
	poss = []
	confirm_neg = []
	confirm_ans = []

	for i in xrange(10):
		if debug:	print "===== try: ", i	# 第幾次嘗試

		if len(poss):
			aa = list( poss[0] )

		my_guess = get_one_elem(aa)	# 隨機取一個作猜測
		while check_guess(confirm_neg, my_guess) == False:
			my_guess = get_one_elem(aa)
		result = get_wawb(answer, my_guess)	# 結果
		if debug:	print my_guess, "=> ", result
		found_pair = find_wawb(aa, result, my_guess)	# 此結果可能的組合
		if debug:	print "len(found_pair): ", len(found_pair)

		if result == [0,0]:	# 恭喜，這四個數字完全不可能
			if debug:	print "these 4 numbers are not possible: ", my_guess
			confirm_neg = my_guess
		else:
			if len(poss) == 0:
				poss.append(found_pair)
			else:
				tmp0 = set(poss[0])
				tmp1 = set(found_pair)
				new_pair = tmp0 & tmp1
				#print "len(new_pair): ", len(new_pair)
				if len(new_pair) == 1:
					if debug:	print "answer is ", new_pair
					confirm_ans = list(new_pair)
					break
				elif len(new_pair) == 0:
					if debug:	print "no intersection ???"
				elif len(new_pair) < 10:
					if debug:	print "left pairs: ", new_pair
				poss[0] = new_pair

	if get_wawb(answer, list( confirm_ans[0] )) == [4,0]:
		print "got answer and checked, try ", i, " times"
		return i

	return 0

# a = [0, 1, 2, ..., 10]
# all_perm = C(10, 4)
all_perm = permutations(range(10), 4)
#dump_all(all_perm)
all_list = list(all_perm)

guess_time = []
for tt in xrange(100):
	answer = get_one_elem(all_list)
	print "answer: ", answer
	guess_time.append( make_wawb_guess(all_list, answer) )

print "max: ", max(guess_time)
print "min: ", min(guess_time)
print "sum: ", sum(guess_time)
print "avg: ", float(sum(guess_time)) / len(guess_time)
