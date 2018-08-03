#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
a simple demo to ultilize function in the other script
'''


from __future__ import print_function
# use shuffle_array() in fisher_yates_shuffle.py
from fisher_yates_shuffle import shuffle_array

REPEAT = 5
NAME_LIST = ['zoo', 'bob', 'tim', 'david', 'pineapple',
             'fred', 'victory', 'limb']

print("original: {}".format(NAME_LIST))

# repeat shuffling
for i in range(5):
    shuffle_array(NAME_LIST)
    print(i, ':', NAME_LIST)
