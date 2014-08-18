#!/usr/bin/python

# python challenge level 6

import re, zipfile

zfile = 'ch.zip'
start = '90052'
history = []

foo = zipfile.ZipFile(zfile, 'r')

idx = start
while True:
	data = foo.read(idx + '.txt');
	m = re.search('(\d+)', data)
	if m != None:
		idx = m.group(1)
		#print idx
		history.append(idx)
	else:
		break

msg = ''
for i in history:
	cmt = foo.getinfo(i+'.txt').comment
	msg = msg + cmt

print msg
'''
print ''.join([foo.getinfo(i+'.txt').comment for i in history])
'''
foo.close()
# oxygen