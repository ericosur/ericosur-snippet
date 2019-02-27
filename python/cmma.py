#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
a stupid python script add ``'`` around every characters
for example, "hello" would be
'h', 'e', 'l', 'l', 'o'

'''

from __future__ import print_function


STR = "the quick smart fox jumps over the lazy dog"

for ch in STR:
    #print('\'', ch, '\'', ',', end=' ')
    print('\'', ch, '\'', ',',)

print()

for ch in STR:
    #print("\'%c\', " % ch, end=' ')
    print("\'%c\', " % ch,)
