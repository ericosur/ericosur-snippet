#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' demo of using raw_input '''

from __future__ import print_function

def demo():
    ''' demo function '''
    name = raw_input('input you name: ')
    print("name: {}".format(name))

    # demo of using getpass
    import getpass
    print("just test, don't answer real password!")
    PW = getpass.getpass('password: ')
    print("PW: {}".format(PW))



if __name__ == '__main__':
    demo()
