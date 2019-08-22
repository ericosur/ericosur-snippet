#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
just a trivia script to use foo-loop and print
if numpy is available, it could be more efficient by using:
np.arange and np.sum
'''

class SumUp():
    ''' different method for sum '''
    def __init__(self):
        self.sum = 0
        self.max_num = 100

    def print_out(self):
        ''' printOut '''
        print("sum from 1 to {} = {}".format(self.max_num, self.sum))

    def sum1(self):
        ''' fill arr '''
        s = 0
        # sum from 0 to 100
        for i in range(self.max_num + 1):
            s += i
        return s

    def sum2(self):
        ''' fill arr '''
        arr = [i for i in range(self.max_num + 1)]
        return sum(arr)

    def test(self):
        ''' test '''
        self.sum = self.sum1()
        self.print_out()
        self.sum = self.sum2()
        self.print_out()


def main():
    '''main function'''
    a = SumUp()
    a.test()

if __name__ == '__main__':
    main()
