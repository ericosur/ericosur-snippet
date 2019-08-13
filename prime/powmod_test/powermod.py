#!/usr/bin/env python3
# coding: utf-8

'''
http://en.wikipedia.org/wiki/Modular_exponentiation
http://reference.wolfram.com/language/ref/PowerMod.html

base ^ exp could be so large to calculate,
use modular_pow to get modulus only

'''

import sys

def modular_pow(base, exp, mod):
    '''
    b, e, m are natural
    '''
    c = 1
    for _ in range(exp):
        c = (c * base) % mod
    return c

def powermod(b, e, m):
    ''' powermod '''
    r0 = modular_pow(b, e, m)
    print('{} ^ {} mod {} = {}'.format(b, e, m, r0))
    # there is a built-in function
    r1 = pow(b, e, m)
    #print('{} ^ {} mod {} = {}'.format(b, e, m, r1))
    assert r0 == r1


def main(argv):
    ''' main '''
    if argv == []:
        print('demo:')
        powermod(4, 13, 497)
        powermod(104857, 32768, 4294)
    else:
        try:
            arr = [int(x) for x in argv]
            (b, e, m) = arr
            powermod(b, e, m)
        except ValueError as err:
            print(err)

if __name__ == '__main__':
    main(sys.argv[1:])
