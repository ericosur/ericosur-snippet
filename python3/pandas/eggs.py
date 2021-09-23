#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' simple csv sample '''

from __future__ import print_function
import os
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
    if os.path.isfile(FILEN):
        print('remove {} first...'.format(FILEN))
        os.remove(FILEN)

    with open(FILEN, 'w', encoding='utf8') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        sw.writerow(get_filled_array())
    csvfile.close()
    print('output {} random numbers to {}'.format(COUNT, FILEN))

if __name__ == '__main__':
    main()
