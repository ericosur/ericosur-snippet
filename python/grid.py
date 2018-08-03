#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
a piece of code translated from MMI project
'''

from __future__ import print_function


def get_next(pos):
    ''' get next position '''
    nextIndex = (2, 0, 1)
    row = pos // 3
    col = pos % 3
    result = nextIndex[row] * 3 + col
    return result

NXT = 0
for _ in range(9):
    NXT = get_next(NXT)
    print(NXT,)
