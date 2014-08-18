#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
題目：
計算 4001 的 5003 次方的未四位數

解答：
在許多場合直接計算會overflow，而問題只要末四位數，所以只取
10000以下的數字作運算即可，也不會overflow，在32bit下，此招
可以用到46340的若干次方

4003**5003 有 41497 個數字 5003 * log10(4007) (無條件進入整數)
'''

base = 4381
radix = 5003
v = base

for i in xrange(radix-1):
	v *= base
	v = v % 10000

print "%d ** %d 的未四位數: %d" % (base, radix, v)
