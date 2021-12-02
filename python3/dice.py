#!/usr/bin/python3
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


class TestDice():
    ''' test sum of dices '''
    num_dice = 3
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
        print(f'from {self.min_sum} to {self.max_sum}')

    def plot_result(self):
        ''' plot '''
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        x = np.arange(self.min_sum, self.max_sum + 1)
        plt.title('title')
        plt.xlabel('sum')
        plt.ylabel('accumulates')
        #sns.set(style='whitegrid')
        for i, y in enumerate(self.ydata):
            plt.plot(x, y, color=colors[i])
        plt.show()

    def method1(self):
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

    def method2(self):
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

    def action(self):
        ''' action '''
        self.print_header()
        self.method1()
        self.method2()
        self.method2()
        self.method2()
        self.method2()
        self.plot_result()

def main():
    ''' main '''
    runTest = TestDice()
    runTest.action()

if __name__ == '__main__':
    main()
