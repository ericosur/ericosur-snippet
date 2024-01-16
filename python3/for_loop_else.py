#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
reference from: http://www.thegeekstuff.com/2017/07/python-for-loop-examples/
'''

from __future__ import print_function


def test_for_loop(checkname):
    ''' lookup checkname from names '''
    found = False
    postfix = "not found"
    names = ["john", "lisa", "raj", "jacob"]
    for nn in names:
        if nn == checkname:
            found = True
            break
    else:
        # will not goes here if break in the middle
        print("==> all items processed at for-loop")

    if found:
        postfix = 'found'

    print(f'\t__{checkname}__ is {postfix}')


def show_list_in_list():
    ''' print list in list '''
    two_sets = [["milk", "monkey", "moonshine"], ["pill", "police", "personality"]]
    for i, word_list in enumerate(two_sets):
        for j, word in enumerate(word_list):
            print(f'({i},{j}): {word}')


if __name__ == "__main__":
    print("test#1 ==>")
    test_for_loop("no-such-name")
    print("test#2 ==>")
    test_for_loop("raj")
    print("list in list ==>")
    show_list_in_list()
