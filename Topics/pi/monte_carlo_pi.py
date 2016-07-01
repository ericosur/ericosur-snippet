#!/usr/bin/env python
'''
Monte Carlo method to calculate pi
from comments of:
http://programmingpraxis.com/2009/10/09/calculating-pi/2/
'''

from random import random

def pi(n):
    return 4*float(sum(1 if (random()**2 + random()**2) <= 1 else 0 for i in range(n)))/n

if __name__ == '__main__':
    print "approx pi =", pi(10**8)

