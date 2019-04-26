#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
try the python static variable and static method
http://stackoverflow.com/questions/68645/python-static-variable
'''

from __future__ import print_function

class MyClass(object):
    '''demo static data member of a python class'''

    val = 3   # looks like a static var, but not similar as C++/Java

    def __init__(self):
        self.val = 100

    @staticmethod
    def show():
        '''static method access static var'''
        print("show(): ", MyClass.val)

    def show2(self):
        '''returns data memeber of object'''
        print("show2(): ", self.val)

def main():
    '''main function'''

    MyClass.show()

    m = MyClass()
    print('m.i = {}'.format(m.val))
    MyClass.val = 5
    m.show2()
    MyClass.show()

if __name__ == '__main__':
    main()
