#!/usr/bin/python
# a piece of code translated from MMI project

def GetNext(pos):
	nextIndex = (2,0,1)
	row = pos // 3
	col = pos % 3
	result = nextIndex[row] * 3 + col
	return result


nxt = 0

for i in range(9):
	nxt = GetNext(nxt)
	print(nxt,)
