#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
reference from http://snippets.dzone.com/posts/show/5433

using Monte Carlo method to calculate Pi
'''

import time
import random
import math

class CalcPi():
    ''' a class to calculate pi from random numbers '''
    def __init__(self):
        self.times = 10000000
        self.i = 0
        self.isnot = 0
        self.start = 0
        self.end = 0

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
        self.start = time.time()
        self.run()
        r = self.get_results()
        pi = r[0] / (r[0] + r[1]) * 4
        self.end = time.time()
        return pi

    def get_duration(self):
        ''' print duration '''
        d = abs(self.start - self.end)
        print(f"duration: {d:.3f} seconds")

def main():
    '''main function'''
    mypi = CalcPi()
    got_pi = mypi.get_pi()
    dist = abs(math.pi - got_pi)
    print(f'got {got_pi} and distance: {dist:.6f}')
    mypi.get_duration()


if __name__ == '__main__':
    print(__doc__)
    main()
