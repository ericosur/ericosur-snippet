#!/usr/bin/env python3
# coding: utf-8

''' class method '''

import math

class MyRect():
    ''' solution '''
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        msg = f'W, H = ({self.width}, {self.height})'
        return msg

    @classmethod
    def get_demo_class(cls):
        ''' get class '''
        print(cls.__name__)
        return cls(10, 10)

    def get_area(self):
        ''' area '''
        return MyRect.calculate_area(self.width, self.height)

    def do_action(self):
        ''' do_action '''
        return math.sqrt((self.width / 2) ** 2 + (self.height / 2) ** 2)

    @staticmethod
    def calculate_area(h, w):
        ''' calculate area '''
        return h * w

class Area(MyRect):
    ''' area '''
    def __init__(self, w=0, h=0):
        super().__init__(w, h)

    # @classmethod
    # def get_demo_class(cls):
    #     ''' get class '''
    #     print(cls.__name__)
    #     return cls()

    @classmethod
    def get_m1(cls):
        ''' get_m1 '''
        m = cls.calculate_area(17, 17)  # better
        n = MyRect.calculate_area(19, 19)   # bad
        return m + n

    def do_action(self):
        ''' override do_action() of super class '''
        m = math.pow(self.width / 4, 2)
        n = math.pow(self.height / 4, 2)
        return math.sqrt(m + n)

def main():
    ''' main '''
    a = Area.get_demo_class()
    print(a.get_area())
    print(a.get_m1())
    print(a.do_action())


if __name__ == '__main__':
    main()
