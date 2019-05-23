#!/usr/bin/env python3
# coding: utf-8
#

'''
how to use Python Singleton
'''

class Singleton(object):
    __single = None
    __inited = False
    def __new__(clz):
        print('__new__')
        if not Singleton.__single:
            print('call object.__new__')
            Singleton.__single = object.__new__(clz)
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
        print('__del__')
        __inited = False

    def __str__(self):
        return '{}'.format(self.value)

    def doSomething(self):
        print("doSomething")

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1


def main():
    s1 = Singleton()
    s1.doSomething()  # do something...XD
    print(s1)
    s1.inc()
    s1.inc()
    print(s1)

    s2 = Singleton()
    s2.doSomething()  # do something...XD
    print(s2)

    print(s1 is s2)  # True

if __name__ == '__main__':
    main()
