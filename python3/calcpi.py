#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
reference from http://snippets.dzone.com/posts/show/5433

using Monte Carlo method to calculate Pi
'''

import math
import random
import time


class CalcPi():
    ''' a class to calculate pi from random numbers '''
    REPEAT_TIME = 10000000

    def __init__(self):
        self.inside = 0
        self.outside = 0
        self.start = 0
        self.end = 0

    @staticmethod
    def is_on_circle(x, y):
        ''' is (x, y) in range of the unit circle '''
        return math.sqrt(x ** 2 + y ** 2) < 1

    def _run_repeat(self):
        ''' repeat random tries '''
        self.outside = 0
        for x in range(CalcPi.REPEAT_TIME):
            x, y = random.random(), random.random()
            if self.is_on_circle(x, y):
                self.inside += 1
            else:
                self.outside += 1

    def get_results(self):
        ''' return results '''
        return (float(self.inside), float(self.outside))

    def get_pi(self):
        ''' return guessed pi '''
        self.start = time.time()
        self._run_repeat()
        r = self.get_results()
        pi = r[0] / (r[0] + r[1]) * 4
        self.end = time.time()
        return pi

    def get_duration(self):
        ''' print duration '''
        d = abs(self.start - self.end)
        print(f"duration: {d:.3f} seconds")

    @classmethod
    def run(cls):
        ''' run '''
        calcpi = cls()
        got_pi = calcpi.get_pi()
        dist = abs(math.pi - got_pi)
        print(f'got {got_pi} and distance: {dist:.6f}')
        calcpi.get_duration()

def main():
    '''main function'''
    print(__doc__)
    CalcPi.run()

if __name__ == '__main__':
    main()
