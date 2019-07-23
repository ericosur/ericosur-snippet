#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' fisher-yates shuffle '''

from __future__ import print_function
import random

# implement fisher-yates shuffle in python

def shuffle_array(arr, debug=False):
    '''shuffle array using fisher'''
    n = len(arr)
    while n > 1:
        k = random.randint(0, n-1)
        n = n - 1
        arr[n], arr[k] = arr[k], arr[n]
        if debug:
            print('k:{} exchange:{} and {}'.format(k, arr[n], arr[k]))
            show_array(arr)

def get_array(max_size=20):
    '''fill array with index, [0, 1, 2, ... max-size-1] '''
    return [i for i in range(0, max_size)]

def show_array(arr):
    '''dump array'''
    print(arr)

def main():
    '''main function'''
    ARRAY_SIZE = 17
    REPEAT = 3

    for _ in range(REPEAT):
        arr = get_array(ARRAY_SIZE)
        copy1 = arr.copy()
        copy2 = arr.copy()
        #show_array(arr)
        shuffle_array(copy1)
        #print "result:",
        show_array(copy1)
        random.shuffle(copy2)
        show_array(copy2)
        print()


if __name__ == '__main__':
    main()
