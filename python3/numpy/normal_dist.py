#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=unused-variable
# pylint: disable=unnecessary-pass
#

'''
using numpy to sample values from a normal distribution
sample from
https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
'''

from __future__ import print_function

import argparse
import sys
import matplotlib.pyplot as plt
import numpy as np


class NormalDistSeed():
    ''' to keep mu, sigma, and size '''
    def __init__(self):
        self._mu = 300
        self._sigma = 50
        self._size = 1000
        self._listeners = []

    @property
    def mu(self):
        ''' getter '''
        return self._mu
    @mu.setter
    def mu(self, val):
        ''' setter '''
        if val and self._mu != val:
            self._mu = val
            self.__notify()
    @property
    def sigma(self):
        ''' getter '''
        return self._sigma
    @sigma.setter
    def sigma(self, val):
        ''' setter '''
        if val and self._sigma != val:
            self._sigma = val
            self.__notify()
    @property
    def size(self):
        ''' getter '''
        return self._size
    @size.setter
    def size(self, val):
        ''' setter '''
        if val and self._size != val:
            self._size = val
            self.__notify()

    def __notify(self):
        ''' something changed '''
        self.do_something()

    def do_something(self):
        ''' child class to override this function '''
        pass



class DrawNormal(NormalDistSeed):
    ''' draw normal distribution '''

    logfile = 'normal_dist.log'

    def __init__(self):
        super().__init__()
        self._drawplot = False
        self._dumpfile = False
        self._verbose = False
        self.data = None
        self.fobj = None

    def show_prop(self):
        ''' str '''
        self.logd(f"properties: {self.mu=}, {self.sigma=}, {self.size=}")

    def log2file(self, *arg, **wargs):
        ''' log 2 file '''
        if self.fobj:
            print(*arg, **wargs, file=self.fobj)

    def logd(self, *arg, **wargs):
        ''' logd '''
        print(*arg, **wargs, file=sys.stderr)

    @property
    def verbose(self):
        ''' getter '''
        return self._verbose
    @verbose.setter
    def verbose(self, val):
        ''' setter '''
        #self.logd('DrawNormal.verbose:', val)
        self._verbose = val
    @property
    def drawplot(self):
        ''' getter '''
        return self._drawplot
    @drawplot.setter
    def drawplot(self, val: bool):
        ''' setter '''
        self._drawplot = val
    @property
    def dumpfile(self):
        ''' getter '''
        return self._dumpfile
    @dumpfile.setter
    def dumpfile(self, val: bool):
        ''' dump setter '''
        self._dumpfile = val

    def dump_text(self):
        ''' dump data as text '''
        if not self.dumpfile:
            return
        self.logd("DrawNormal.dump_text()...")
        # here I convert to int32, origin is float
        results = np.int32(self.data)
        with open(self.logfile, "wt", encoding='UTF-8') as self.fobj:
            for i in results.tolist():
                # one value per line
                self.log2file(i)
        self.logd("output to:", self.logfile)

    def draw_plot(self):
        ''' draw the plot '''
        if not self.drawplot:
            return
        self.logd("DrawNormal.draw_plot()...")
        count, bins, ignored = plt.hist(self.data, self.size, density=True)
        plt.plot(bins, 1/(self.sigma * np.sqrt(2 * np.pi)) *
                 np.exp(-(bins - self.mu)**2 / (2 * self.sigma**2)),
                 linewidth=2, color='r')
        plt.show()

    def do_something(self):
        ''' do something '''
        if self.verbose:
            self.show_prop()
            #self.data = np.random.normal(self.mu, self.sigma, self.size)
            #self.draw_plot()
        #else:
            #self.logd("DrawNormal.do_something: value changed...")


    def action(self):
        ''' action '''
        if self.dumpfile or self.drawplot:
            self.data = np.random.normal(self.mu, self.sigma, self.size)
        else:
            self.logd("DrawNormal: will not generate data...")
            self.show_prop()
        self.dump_text()
        self.draw_plot()

    @classmethod
    def run(cls, args):
        ''' run me '''
        obj = cls()
        obj.verbose = args.verbose
        obj.drawplot = args.draw
        obj.dumpfile = args.dump
        obj.mu = args.mu
        obj.sigma = args.sigma
        obj.size = args.size
        obj.action()


def main():
    ''' main function '''
    parser = argparse.ArgumentParser(description='''
        Use numpy to generate some integers and plot
    ''', usage='normal_dist.py -n 29999 --draw')
    parser.add_argument("--draw", dest='draw', action='store_true', default=False,
        help='draw this series of numbers')
    parser.add_argument("--dump", dest='dump', action='store_true', default=False,
        help='dump numbers into file')
    parser.add_argument("--mu", type=int, dest='mu',
        help='specify the mean value of normal distribution series')
    parser.add_argument("--sigma", type=int, dest='sigma',
        help='specify the sigma of normal distribution series')
    parser.add_argument("--size", type=int, dest='size',
        help='specify the size of normal distribution series')
    parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', default=False,
        help='verbose mode')
    parser.add_argument("-d", "--debug", action='store_true', default=False,
        help='debug mode')

    args = parser.parse_args()
    DrawNormal.run(args)


if __name__ == '__main__':
    main()
