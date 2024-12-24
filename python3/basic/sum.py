#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
just a trivia script to use foo-loop and print
if numpy is available, it could be more efficient by using:
np.arange and np.sum
'''

from time import perf_counter as pc
from time import sleep
from functools import reduce
import numpy as np

class Solution():
    ''' basic flow '''
    def __init__(self, max_num):
        self.sum = 0
        self.duration = 0
        self.max_num = max_num

    def print_out(self):
        ''' printOut '''
        print(f"sum from 1 to {self.max_num} = {self.sum}, ", end='')
        print(f"takes {self.duration * 1000:.3f} ms")

    @staticmethod
    def do_work():
        ''' just sleep 500 ms '''
        print('sleep 0.5 seconds')
        sleep(0.5)
        return 0

    def do_something(self, func=None):
        ''' do '''
        start = pc()

        if func is None:
            self.sum = self.do_work()
        else:
            self.sum = func()

        self.duration = pc() - start
        self.print_out()

class SumUp(Solution):
    ''' different method for sum '''
    def __init__(self, max_num=9_999_999):
        super().__init__(max_num)

    def sum1(self):
        ''' using for-loop to sum up '''
        print("sum1: for-loop to sum up")
        s = 0
        for i in range(self.max_num + 1):
            s += i
        return s

    def sum2(self):
        ''' using list() and sum() '''
        print("sum2: built-in sum(List[int])")
        arr = list(range(self.max_num + 1))
        return sum(arr)

    def sum3(self):
        ''' using np.sum '''
        print("sum3: numpy.sum")
        # np.arange fill an array with inc/dec numbers
        arr = np.arange(1, self.max_num + 1)
        return np.sum(arr)

    # pylint not recommend this method
    # it suggests (consider-using-generator) --OR--
    # Unnecessary use of a comprehension (unnecessary-comprehension)
    # def sum4(self):
    #     ''' using list comprehension '''
    #     print("sum4: list comprehension")
    #     return sum([i for i in range(self.max_num + 1)])

    def sum5(self):
        ''' using generator expression '''
        print("sum5: generator expression")
        return sum(i for i in range(self.max_num + 1))

    def sum6(self):
        ''' using functools.reduce '''
        print("sum6: functools.reduce")
        return reduce(lambda x, y: x + y, range(self.max_num + 1))

    def test(self):
        ''' test '''
        self.do_something()
        self.do_something(self.sum1)
        self.do_something(self.sum2)
        self.do_something(self.sum3)
        #self.do_something(self.sum4)
        self.do_something(self.sum5)
        self.do_something(self.sum6)

def main():
    '''main function'''
    a = SumUp()
    a.test()

if __name__ == '__main__':
    main()
