#!/usr/bin/python
# coding: utf-8

''' need check '''

from urllib.request import urlopen
import pickle

def main():
    ''' main '''

    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    obj = pickle.load(urlopen(url))
    for line in obj:
        print(''.join(map(lambda pair: pair[0]*pair[1], line)))
