#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
to find four-digit vampire numbers

http://en.wikipedia.org/wiki/Vampire_number
'''

from __future__ import print_function

from itertools import permutations  # , combinations


def find_vampire_in_4digit(num):
    '''give number check if a vampire number'''
    digit = 4
    nl = list(str(num))
    if len(nl) != digit:
        print('only works for 4-digit number!')
        return

    vampires = []
    jj = permutations(nl, digit)
    #jj = combinations(nl, 4)
    for cc in jj:
        n1 = int(cc[0] + cc[1])
        n2 = int(cc[2] + cc[3])
        if n1 > n2:
            n1, n2 = n2, n1
        if n1 * n2 == num:
            if num in vampires:
                continue
            print(str(num) + " is a vampire number! " + str(n1) + " x " + str(n2))
            vampires.append(num)


def main():
    '''main function'''
    for val in range(1000, 9999):
        find_vampire_in_4digit(val)


if __name__ == '__main__':
    main()
