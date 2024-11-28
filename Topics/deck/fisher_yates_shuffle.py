#!/usr/bin/env python3
# coding: utf-8

''' implement fisher-yates shuffle in python '''

import random


def shuffle_array(arr):
    ''' shuffle array '''
    n = len(arr)
    while n > 1:
        k = random.randint(0, n-1)
        n = n - 1
        arr[n], arr[k] = arr[k], arr[n]

def show_array(arr):
    ''' show array '''
    print(arr)

def main():
    ''' main '''
    arr = list(range(20))
    show_array(arr)
    shuffle_array(arr)
    show_array(arr)

if __name__ == '__main__':
    main()
