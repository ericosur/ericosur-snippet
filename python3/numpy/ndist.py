#!/usr/bin/env python3
# coding: utf-8
#
# py//lint: disable=unused-variable
# py//lint: disable=unnecessary-pass
# pylint: disable=too-many-instance-attributes
#

'''
using numpy to sample values from a normal distribution
sample from
https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
'''


import sys
import time
from typing import Annotated
import numpy as np
from pydantic import BaseModel
import typer

sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "python/")
from myutil import prt, read_jsonfile  # type: ignore[import]

class Dist(BaseModel):
    ''' Dist '''
    mu: float
    sigma: float
    size: int

class NormalDistData():
    ''' to keep mu, sigma, and size '''
    def __init__(self, dist: Dist):
        self.dist = dist
        self.rng = np.random.default_rng(int(time.time()))
        self.data = None
        self.__fill_stdnorm()

    def __fill_stdnorm(self):
        ''' fill buffer '''
        self.data = self.dist.mu + self.dist.sigma * self.rng.standard_normal(size=self.dist.size)



def main(
        conf: Annotated[str, typer.Option("--conf",
                                            help="json file with dist data")] = "dist.json",
        _csv: Annotated[str, typer.Option("--csv", help="output to csv file")] = "d.csv",
):
    ''' main function '''
    prt(conf)
    d = read_jsonfile(conf)
    mu = d.get('mu', 300)
    sigma = d.get('sigma', 50)
    size = d.get('size', 1000)
    dist = Dist(mu=mu, sigma=sigma, size=size)
    prt(dist)
    ndd = NormalDistData(dist)
    prt(ndd.data)


if __name__ == '__main__':
    typer.run(main)
