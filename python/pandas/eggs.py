#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' simple csv sample '''

from __future__ import print_function
import csv
import random

COUNT = 10

def get_filled_array():
    '''get ten random numbers'''
    arr = []
    for _ in range(COUNT):
        arr.append(random.randint(0, 99))
    return arr

def main():
    '''main function'''
    FILEN = 'eggs.csv'
    with open(FILEN, 'wb') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        sw.writerow(get_filled_array())
    print('output {} random numbers to {}'.format(COUNT, FILEN))

if __name__ == '__main__':
    main()
