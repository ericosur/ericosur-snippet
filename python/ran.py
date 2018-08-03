#!/usr/bin/python
# -*- coding: utf-8 -*-
#
''' just pick one name from name list randomly '''

from __future__ import print_function
import random

def demo():
    '''demo function'''
    name_list = ['alice', 'bob', 'cathy', 'david', 'eric',
                 'fred', 'grace', 'helen']
    size = len(name_list)
    REPEAT = 5

    for _ in range(REPEAT):
        idx = random.randint(0, size - 1) # int(random.random() * size)
        print("name picked: {}".format(name_list[idx]))

if __name__ == '__main__':
    demo()
