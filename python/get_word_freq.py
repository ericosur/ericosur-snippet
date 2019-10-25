#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' get_word_freq from files '''

import sys
import re
from operator import itemgetter

def readfile(f):
    ''' read file '''
    with open(f, "r") as pFile:
        return pFile.read()

def divide(c, regex):
    ''' the regex below is only valid for utf8 coding '''
    return regex.findall(c)


def update_dict(di, li):
    ''' update_dict from di, li '''
    for i in li:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    return di

def main(files):
    ''' main function '''

    #regex compile only once
    regex = re.compile(r"(?x) (?: [\w-]+  | [\x80-\xff]{3} )")

    mydict = {}

    #get all words from files
    for f in files:
        words = divide(readfile(f), regex)
        mydict = update_dict(mydict, words)

    #sort dictionary by value
    mydict = sorted(mydict.items(), key=itemgetter(1), reverse=True)

    #output to standard-output
    for i in mydict:
        print(i[0], i[1])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print('specify file name from CLI...')
