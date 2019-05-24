#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
just a trivia script to use foo-loop and print
if numpy is available, it could be more efficient by using:
np.arange and np.sum
'''

from __future__ import print_function

class SumUp(object):
    def __init__(self):
        self.sum = 0
        self.max_num = 100

    def printOut(self):
        print("sum from 1 to {} = {}".format(self.max_num, self.sum))

    def sum1(self):
        s = 0
        # sum from 0 to 100
        for i in range(self.max_num + 1):
            s += i
        return s

    def sum2(self):
        arr = [ i for i in range(self.max_num + 1)]
        return sum(arr)

    def test(self):
        self.sum = self.sum1()
        self.printOut()
        self.sum = self.sum2()
        self.printOut()


def main():
    '''main function'''
    a = SumUp()
    a.test()

if __name__ == '__main__':
    main()
