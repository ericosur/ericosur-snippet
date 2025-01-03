#!/usr/bin/env python
# coding: utf-8

'''
pymc tutorial
'''

# pylint: disable=import-error

import arviz as az  # type: ignore[import]
import matplotlib.pyplot as plt
import numpy as np


def main():
    ''' main '''
    #%config InlineBackend.figure_format = 'retina'
    # Initialize random number generator
    RANDOM_SEED = 8927
    rng = np.random.default_rng(RANDOM_SEED)
    az.style.use("arviz-darkgrid")

    # True parameter values
    alpha, sigma = 1, 1
    beta = [1, 2.5]

    # Size of dataset
    size = 100

    # Predictor variable
    X1 = np.random.randn(size)
    X2 = np.random.randn(size) * 0.2

    # Simulate outcome variable
    Y = alpha + beta[0] * X1 + beta[1] * X2 + rng.normal(size=size) * sigma

    _, axes = plt.subplots(1, 2, sharex=True, figsize=(10, 4))
    axes[0].scatter(X1, Y, alpha=0.6)
    axes[1].scatter(X2, Y, alpha=0.6)
    axes[0].set_ylabel("Y")
    axes[0].set_xlabel("X1")
    axes[1].set_xlabel("X2")

    plt.show()

if __name__ == '__main__':
    main()
