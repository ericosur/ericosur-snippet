#!/usr/bin/env python3
# coding: utf-8

'''
# Copyright (c) 2009 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?action=history&offset=20081029005339
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?oldid=15344
'''

# pylint: disable=invalid-name
#
import random
import sys

def miller_rabin_pass(a, n):
    ''' miller_rabin_pass '''
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for _ in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    ''' miller_rabin '''
    for _ in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, n):
            return False
    return True


def test_and_print(values):
    ''' test_and_print '''
    if not values:
        values.append(795028841)

    for v in values:
        try:
            n = int(v)
            print('{} is {}'.format(n, miller_rabin(n) and "PRIME" or "COMPOSITE"))
        except ValueError:
            print('{} is not valid'.format(v))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "test":
            test_and_print(sys.argv[2:])
            sys.exit(0)

        if sys.argv[1] == "genprime":
            nbits = 32
            while True:
                p = random.randrange(2 ** nbits)
                if p % 2 == 0:
                    continue
                if p % 3 == 0:
                    continue
                if p % 5 == 0:
                    continue
                if p % 7 == 0:
                    continue
                if miller_rabin(p):
                    print(p)
                    break
        sys.exit(0)

    print('usage: 1) MillerRabin.py test <integer>')
    print('usage: 2) MillerRabin.py genprime')
    print('\n...demo...')
    test_and_print([])
