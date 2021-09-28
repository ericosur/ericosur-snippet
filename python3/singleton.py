#!/usr/bin/env python3
# coding: utf-8
#

'''
how to use Python Singleton
'''
from __future__ import print_function

# pylint: disable=useless-object-inheritance
class Singleton(object):
    ''' single class usage '''
    __single = None
    __inited = False
    def __new__(cls):
        ''' new '''
        print('__new__')
        if not Singleton.__single:
            print('call object.__new__')
            Singleton.__single = object.__new__(cls)
        return Singleton.__single

    def __init__(self):
        '''
        after __new__ excuted, then __init__
        use '__inited' to prevent re-initialize **value**
        '''
        print('__init__')
        if not Singleton.__inited:
            print('do init...')
            Singleton.__inited = True
            self.value = 0

    def __del__(self):
        ''' dtor '''
        print('__del__')
        __inited = False

    def __str__(self):
        ''' stringify '''
        return str(self.value)

    @staticmethod
    def do_something():
        ''' test function '''
        print("do_something")

    def inc(self):
        ''' increase value '''
        self.value += 1

    def dec(self):
        ''' decrease value '''
        self.value -= 1


def main():
    ''' main test function '''
    s1 = Singleton()
    s1.do_something()  # do something...XD
    print(s1)
    s1.inc()
    s1.inc()
    print(s1)

    s2 = Singleton()
    s2.do_something()  # do something...XD
    print(s2)

    print(s1 is s2)  # True

if __name__ == '__main__':
    main()
