#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
''' just pick one name from name list randomly '''

import random


def demo():
    '''demo function'''
    name_list = ['alice', 'bob', 'cathy', 'david', 'eric',
                 'fred', 'grace', 'helen', 'injet', 'jacob',
                 'keem', 'liam', 'mike', 'nike']
    size = len(name_list)
    REPEAT = 2

    print('use random.randint as index:')
    for _ in range(REPEAT):
        idx = random.randint(0, size - 1) # int(random.random() * size)
        print(f"name picked: {name_list[idx]}")

    # another way
    print('use random.choice:')
    for _ in range(REPEAT):
        print(f"name picked: {random.choice(name_list)}")

if __name__ == '__main__':
    demo()
