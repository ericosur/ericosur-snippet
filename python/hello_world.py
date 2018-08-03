#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
	this file needs to be stored as UTF-8 text file
'''

from __future__ import print_function

def main():
    '''main function'''
    msg = "哈囉"

    # as big5
    print(msg.decode('utf8').encode('big5'))
    # utf-8
    print(msg)

if __name__ == '__main__':
    main()
