#!/usr/bin/python
# -*- coding: utf-8 -*-

""" this script is a practice to recursive print out a
    list """

from __future__ import print_function

def print_lol(the_list):
    """ this function will recursive to print list """

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

if __name__ == '__main__':
    MOVIES = ["the holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
              ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam",
                                  "Eric Idle", "Terry Jones"]]]
    print_lol(MOVIES)
