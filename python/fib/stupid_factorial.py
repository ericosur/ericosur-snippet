#!/usr/bin/env python3
# coding: utf-8

''' stupid to calculate n! '''

import sys
import math

def stupid_factorial(m):
    '''
    a trivia way to get n! recursively
    '''
    if m <= 1:
        return 1

    return m * stupid_factorial(m - 1)


def try3k(n):
    ''' try3k '''
    # maybe too deep recursive to calculate n!
    #n = 3000 # try to get n!

    '''
    try to use Stirling's approximation for value of n!
    n! ~ sqrt(2*pi*n)*(n/e)^n
    but (n/e)^n is too large

    try to know how many digits for n!
    log10(n!) ~ log10(sqrt(2*pi*n)) + n * log10(n/e)

    '''
    val = math.log10(math.sqrt(2 * math.pi * n)) + n * math.log10(n / math.e)
    print("estimated digits length of {}! = {}".format(n, math.ceil(val)))

def get_digit_len(n):
    ''' get ceiling( log10(n) ) '''
    return math.ceil(math.log10(n))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        try3k(3000)

    for v in sys.argv[1:]:
        try:
            intv = int(v)
            ans = stupid_factorial(intv)
            print("{}! = {}\ndigit len: {}".format(intv, ans, get_digit_len(ans)))
            try3k(intv)
        except ValueError as e:
            print('cannot translate into integer', e)
