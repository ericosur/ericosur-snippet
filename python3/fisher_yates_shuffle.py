#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' fisher-yates shuffle '''

from __future__ import print_function
import random

# implement fisher-yates shuffle in python
MAX_SIZE = 5
SHOW_STEP = 0
REPEAT = 1000

def shuffle_array(arr):
    '''shuffle array using fisher'''
    n = len(arr)
    while n > 1:
        k = random.randint(0, n-1)
        n = n - 1
        arr[n], arr[k] = arr[k], arr[n]
        if SHOW_STEP:
            print('k:{} exchange:{} and {}'.format(k, arr[n], arr[k]))
            show_array(arr)

def fill_array(arr, max_size=20):
    '''fill array with index'''
    for i in range(0, max_size):
        arr.append(i)

def show_array(arr):
    '''dump array'''
    print(arr)

def main():
    '''main function'''
    n = REPEAT
    while n > 0:
        arr = []
        fill_array(arr, MAX_SIZE)
        #show_array(arr)
        shuffle_array(arr)
        #print "result:",
        show_array(arr)
        n = n - 1

if __name__ == '__main__':
    main()
