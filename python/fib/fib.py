#!/usr/bin/python3

import random

''' a simple and stupid fib function test
'''

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# it is time/memory consuming while n is large
if __name__ == '__main__':
    for i in range(10):
        n = random.randint(2,100)
        print('fib({}) = {}'.format(n, fib(n)))
