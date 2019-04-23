#!/usr/bin/env python3

import sys
import math

def stupid_factorial(m):
    '''
    a trivia way to get n! recursively
    '''
    if m <= 1:
        return 1
    else:
        return m * stupid_factorial(m - 1)


def try3k():
    # maybe too deep recursive to calculate n!
    n = 3000 # try to get n!

    '''
    try to use Stirling's approximation for value of n!
    n! ~ sqrt(2*pi*n)*(n/e)^n
    but (n/e)^n is too large

    try to know how many digits for n!
    log10(n!) ~ log10(sqrt(2*pi*n)) + n * log10(n/e)

    '''
    val = math.log10(2 * math.pi * n) + n * math.log10(n / math.e)
    print("log10({}!) = {}".format(n, math.ceil(val)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for v in sys.argv[1:]:
            try:
                n = int(v)
                print("{}! = {}".format(n, stupid_factorial(n)))
            except:
                print("shit happens for:", v)
                quit()
    else:
        try3k()
