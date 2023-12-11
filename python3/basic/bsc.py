#!/usr/bin/env python
# coding: utf-8

'''
from chatgpt
ask about Bayesian Curve

I update this script for newer version of pymc
'''

import matplotlib.pyplot as plt
import pymc as pm

import numpy as np

# 生成一些虛構的數據
np.random.seed(42)
X = np.random.rand(100)
Y = 2 * X + 1 + 0.1 * np.random.randn(100)

# 使用貝葉斯統計學進行線性回歸
with pm.Model() as model:
    # 定義模型
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    beta = pm.Normal('beta', mu=0, sigma=10)
    epsilon = pm.HalfCauchy('epsilon', 5)

    mu = alpha + beta * X
    Y_obs = pm.Normal('Y_obs', mu=mu, sigma=epsilon, observed=Y)

    # 進行 MCMC 採樣
    trace = pm.sample(2000, tune=1000, return_inferencedata=True)

# 繪製貝葉斯曲線
#plt.figure(figsize=(10, 6))
pm.plot_trace(trace)
plt.tight_layout()
plt.show()
