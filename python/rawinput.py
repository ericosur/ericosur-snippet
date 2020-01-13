#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' demo of using raw_input '''

from __future__ import print_function
import getpass

def demo():
    ''' demo function '''
    name = input('input you name: ')
    print("name: {}".format(name))

    # demo of using getpass
    print("just test, don't answer real password!")
    PW = getpass.getpass('password: ')
    print("PW: {}".format(PW))



if __name__ == '__main__':
    demo()
