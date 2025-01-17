#!/usr/bin/env python3
# coding: utf-8

'''
throw __max_dice__ dices (of which point from **min_dice** to **max_dice**)
get the sum
__repeat__ times
plot the result

'''

import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False
from myutil import do_nothing

prt = rprint if USE_RICH else print
DEBUG = True
if DEBUG:
    logd = logger.debug if USE_LOGGER else print
else:
    logd = do_nothing


class TestDice():
    ''' test sum of dices '''
    num_dice = 6
    min_dice = 1
    max_dice = 6
    repeat = 50000

    def __init__(self):
        self.min_sum = self.num_dice * self.min_dice
        self.max_sum = self.num_dice * self.max_dice
        self.size_of_result = self.num_dice*self.max_dice + 1
        self.result = None
        # np's random number generator
        self.rng = np.random.default_rng(int(time.time()))
        self.ydata = []

    def reset_result(self):
        ''' reset all value in result as zero '''
        self.result = np.zeros(self.size_of_result, dtype='uint32')

    def print_header(self):
        ''' print header '''
        prt(f'Use {self.num_dice} dices, total sum from {self.min_sum} to {self.max_sum}')
        prt(f'no of repeat: {self.repeat:,}')

    def plot_result(self) -> None:
        ''' plot '''
        logd('plot results')
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        x = np.arange(self.min_sum, self.max_sum + 1)
        plt.title('title')
        plt.xlabel('sum')
        plt.ylabel('accumulates')
        #sns.set(style='whitegrid')
        for i, y in enumerate(self.ydata):
            plt.plot(x, y, color=colors[i])
        plt.show()

    def method1(self) -> None:
        ''' method 1 '''
        self.reset_result()
        start = time.time()
        for _ in range(self.repeat):
            # max_point_dice need to add one more
            buffer = self.rng.integers(self.min_dice, self.max_dice+1,
                self.num_dice, dtype='uint32')
            s = np.sum(buffer)
            self.result[s] += 1
        duration = time.time() - start
        print(f'duration: {duration:.3f} sec')
        print(self.result[self.min_sum:])
        assert np.sum(self.result) == self.repeat
        self.ydata.append(self.result[self.min_sum:])

    def method2(self) -> None:
        ''' method 2 '''
        self.reset_result()
        start = time.time()
        for _ in range(self.repeat):
            s = 0
            for _ in range(self.num_dice):
                r = randint(1, 6)
                s += r
            self.result[s] += 1
        duration = time.time() - start
        print(f'duration: {duration:.3f} sec')
        print(self.result[self.min_sum:])
        assert np.sum(self.result) == self.repeat
        self.ydata.append(self.result[self.min_sum:])

    def action(self) -> None:
        ''' action '''
        self.print_header()
        self.method1()
        for _ in range(4):
            self.method2()
        self.plot_result()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    TestDice.run()

if __name__ == '__main__':
    main()
