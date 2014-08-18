#!/usr/bin/env python

'''
a demo to use sympy
'''

from sympy import *

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
x = Symbol('x')

f = a*x*x + b*x + c
f = 0
sol = solve(f, x)

pprint(f)
pprint(x)

