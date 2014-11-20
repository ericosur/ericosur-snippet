#!/usr/bin/python

# count char in a string
# Jan 17 2005 by rasmus

s = 'the quick brown fox jumps over the lazy dog'

beg = ord('a')
end = ord('z') + 1

char_no_space = len(s) - s.count(' ')
total = 0

for i in range(beg, end):
    ch = chr(i)
    cnt = s.count(ch)
    percent = cnt / float(char_no_space) *100
    total = total + cnt
    print('%c appears %d times %.2f%%' % (ch, cnt, percent))

print('total count: %d' % total)
