#!/usr/bin/env python

'''
use pollard rho brent method to factorize an integer
'''

import sys
import random

def gcd(m, n):
	'''
	calculate gcd number by rescursive
	'''
	if n == 0:
		return m
	else:
		return gcd(n, m % n)

def brent(N):
    '''
    refer to:
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    http://en.wikipedia.org/wiki/Cycle_detection
    '''
    if N%2==0:
        return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%N+c)%N
                q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break

    return g

def demo():
    '''
        demo function to factorize random numbers
    '''
 
    '''
    the following n is a large prime will take a while to know the result
    n = 1238926361552897
    '''
    rep = 5
    for i in range(rep):
        n = random.randint(0x1419a9a8, 0x4d95a41b)
        n = 2*n + 1    # make sure number is odd
        print "%d: " % (n)
        fact = factorize(n)
        print fact;


def factorize(n):
    '''
        factorize n, return factors in list
    '''
    factors = []
    while (True):
        b = brent(n)
        factors.append(b)
        if (b == n):
            break
        n = n / b
    factors.sort()
    return factors


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for v in sys.argv[1:]:
            try:
                n = int(v)
                print n,": ",
                print factorize(n)
            except:
                print "shit happens for:", v
                quit()
    else:
        demo()

