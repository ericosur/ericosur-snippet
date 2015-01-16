#!/usr/bin/env python
# reference:
# https://comeoncodeon.wordpress.com/2010/09/18/miller-rabin-primality-test/
#

import random

def modulo(a,b,c):
    x = 1
    y = a
    while b>0:
        if b%2==1:
            x = (x*y)%c
        y = (y*y)%c
        b = b/2
    return x%c

def millerRabin(n, iteration):
    if n<2:
        return False
    if n!=2 and n%2==0:
        return False

    d = n - 1
    while d%2 == 0:
        d = d / 2
    for i in range(iteration):
        a = random.randint(1, n-1)
        temp = d
        #x = modulo(a, temp, n)
        x = pow(a, temp, n)     # use built-in function
        while (temp != n-1 and x!=1 and x!=n-1):
            x = (x*x)%n
            temp = temp * 2
        if (x!=n-1 and temp%2==0):
            return False
    return True

if __name__ == '__main__':
    '''
    for i in xrange(10):
        (a, b, n) = (random.randint(70,100), random.randint(40,80), random.randint(41, 97))
        print "pow(%d, %d, %d) = %d" % (a, b, n, pow(a, b, n))
        print "pow(%d, %d, %d) = %d" % (a, b, n, modulo(a, b, n))
    '''
    n = 795028841
    print n, 'is', (millerRabin(n, 20) and "PRIME" or "COMPOSITE")

