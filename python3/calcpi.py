#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
refercenc from http://snippets.dzone.com/posts/show/5433
'''

from __future__ import print_function
import random
import math

# pylint: disable=useless-object-inheritance
class CalcPi(object):
    ''' a class to calculate pi from random numbers '''
    def __init__(self):
        self.times = pow(10, 6)
        self.i = 0
        self.isnot = 0

    @staticmethod
    def is_on_circle(x, y):
        ''' is (x, y) in range of the unit circle '''
        return math.sqrt(x ** 2 + y ** 2) < 1

    def run(self):
        ''' repeat random tries '''
        for x in range(self.times):
            x, y = random.random(), random.random()
            if self.is_on_circle(x, y):
                self.i += 1
            else:
                self.isnot += 1

    def get_results(self):
        ''' return results '''
        return (float(self.i), float(self.isnot))

    def get_pi(self):
        ''' return guessed pi '''
        self.run()
        r = self.get_results()
        return r[0] / (r[0] + r[1]) * 4

def main():
    '''main function'''
    mypi = CalcPi()
    got_pi = mypi.get_pi()
    dist = abs(math.pi - got_pi)
    print('got {} and distance: {}'.format(got_pi, dist))


if __name__ == '__main__':
    main()
