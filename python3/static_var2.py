#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
try the python static variable and static method
http://stackoverflow.com/questions/68645/python-static-variable

add getter & setter
'''

class Foo():
    '''demo static data member of a python class'''
    _i = 97

    def get_i(self):
        ''' getter '''
        return type(self)._i

    def set_i(self, val):
        ''' setter '''
        type(self)._i = val

    i = property(get_i, set_i)


def show():
    ''' show '''
    x1 = Foo()
    print('>>>>> show: x1: ', x1.i)
    x1.i = x1.i + x1.i // 5
    print('<<<<<< show: x1: ', x1.i)

def main():
    '''main function'''
    m1 = Foo()
    print('main: foo: ', m1.i)
    show()
    print('main: foo: ', m1.i)
    if m1.i > 100:
        m1.i = m1.i % 100
    print('main: foo: ', m1.i)
    show()


if __name__ == '__main__':
    main()
