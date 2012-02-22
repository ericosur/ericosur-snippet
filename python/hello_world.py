#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
	this file needs to be stored as UTF-8 text file
'''
foo = "哈囉"

# as big5
print(foo.decode('utf8').encode('big5'))
# utf-8
print(foo);

