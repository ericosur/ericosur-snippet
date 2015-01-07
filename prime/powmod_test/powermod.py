#!/usr/bin/env python

import sys

'''
http://en.wikipedia.org/wiki/Modular_exponentiation
http://reference.wolfram.com/language/ref/PowerMod.html

base ^ exp could be so large to calculate,
use modular_pow to get modulus only

'''

def modular_pow(base, exp, mod):
    '''
    b, e, m are natural
    '''
    c = 1
    for i in xrange(exp):
        c = (c * base) % mod
    return c

def powermod(b,e,m):
    r = modular_pow(b,e,m)
    print "%d ^ %d mod %d = %d" % (b, e, m, r)
    # there is a built-in function
    r = pow(b,e,m)
    print "%d ^ %d mod %d = %d" % (b, e, m, r)


def demo():
    powermod(4,13,497)
    powermod(104857,32768,4294)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        [b,e,m] = sys.argv[1:]
        try:
            powermod(int(b),int(e),int(m))
        except:
            print "shit happens"
            quit()
    else:
        demo()

