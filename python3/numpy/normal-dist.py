#!/usr/bin/env python3
# coding: utf-8
#

'''
using numpy to sample values from a normal distribution
sample from
https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    mu, sigma = 100, 15
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
        np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
        linewidth=2, color='r')
    plt.show()


if __name__ == '__main__':
    main()
