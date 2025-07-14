#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
''' just pick one name from name list randomly '''

import random
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

def demo():
    '''demo function'''
    name_list = ['alice', 'bob', 'cathy', 'david', 'eric',
                 'fred', 'grace', 'helen', 'injet', 'jacob',
                 'keem', 'liam', 'mike', 'nike']
    size = len(name_list)
    REPEAT = 2

    prt('use random.randint as index:')
    for _ in range(REPEAT):
        idx = random.randint(0, size - 1) # int(random.random() * size)
        prt(f"name picked: {name_list[idx]}")

    # another way
    prt('use random.choice:')
    for _ in range(REPEAT):
        prt(f"name picked: {random.choice(name_list)}")

if __name__ == '__main__':
    demo()
