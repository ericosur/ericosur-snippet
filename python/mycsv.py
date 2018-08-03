#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' simple csv sample '''

from __future__ import print_function
import csv
import random

def get_filled_array():
    '''get ten random numbers'''
    ten = 10
    arr = []
    for _ in xrange(ten):
        arr.append(random.randint(0, 99))
    return arr

def main():
    '''main function'''
    with open('eggs.csv', 'wb') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        sw.writerow(get_filled_array())

if __name__ == '__main__':
    main()
