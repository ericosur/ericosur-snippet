#!/usr/bin/python
# -*- coding: utf-8 -*-

''' get_word_freq '''

#author:         rex
#blog:           http://iregex.org
#filename        counter.py
#created:        Mon Sep 20 21:00:52 2010
#desc:           convert .py file to html with VIM.

from __future__ import print_function
import sys
import re
from operator import itemgetter

def readfile(f):
    ''' read file '''
    with file(f, "r") as pFile:
        return pFile.read()

def divide(c, regex):
    ''' the regex below is only valid for utf8 coding '''
    return regex.findall(c)


def update_dict(di, li):
    ''' update_dict from di, li '''
    for i in li:
        if di.has_key(i):
            di[i] += 1
        else:
            di[i] = 1
    return di

def main():
    ''' main function '''
    #receive files from bash
    files = sys.argv[1:]

    #regex compile only once
    regex = re.compile(r"(?x) (?: [\w-]+  | [\x80-\xff]{3} )")

    mydict = {}

    #get all words from files
    for f in files:
        words = divide(readfile(f), regex)
        mydict = update_dict(mydict, words)

    #sort dictionary by value
    #dict is now a list.
    mydict = sorted(mydict.items(), key=itemgetter(1), reverse=True)

    #output to standard-output
    for i in mydict:
        print(i[0], i[1])

if __name__ == '__main__':
    main()
