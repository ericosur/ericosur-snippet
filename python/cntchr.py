#!/usr/bin/python

''' count char in a string '''


from __future__ import print_function

STR = 'the quick brown fox jumps over the lazy dog'

BEG = ord('a')
END = ord('z') + 1

CHAR_NO_SPACE = len(STR) - STR.count(' ')
TOTAL = 0

for i in range(BEG, END):
    ch = chr(i)
    cnt = STR.count(ch)
    percent = cnt / float(CHAR_NO_SPACE) *100
    TOTAL = TOTAL + cnt
    print('%c appears %d times %.2f%%' % (ch, cnt, percent))

print('total count: %d' % TOTAL)
