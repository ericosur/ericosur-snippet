#!/usr/bin/python3
# coding: utf-8

'''
[OEIS A002144](https://oeis.org/A002144)

Pythagorean primes: primes of form 4*k + 1.

5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149, 157, 173,
181, 193, 197, 229, 233, 241, 257, 269, 277, 281, 293, 313, 317, 337, 349, 353,
373, 389, 397, 401, 409, 421, 433, 449, 457, 461, 509, 521, 541, 557, 569, 577,
593, 601, 613, 617

'''

import math
import sys

try:
    sys.path.insert(0, "../../prime")
    from store_prime import StorePrime
except ImportError:
    print('cannot import StorePrime')
    sys.exit(1)

class Solution():
    ''' test if prime '''
    def __init__(self):
        self._sp = StorePrime()
        self._sp.load_pickle()
        self.answers = []

    @staticmethod
    def split_square(p):
        ''' split_square '''
        #print('input: {}'.format(p))
        root = math.floor(math.sqrt(p))
        for i in range(1, root):
            t = p - i * i
            r = math.sqrt(t)
            r_f = math.floor(r)
            if r == r_f:
                #print('{} = {}^2 + {}^2'.format(p, i, int(r)))
                break
        return (p, i, int(r))

    def run(self):
        ''' run '''
        primes = self._sp.get_primes_less_than(618)
        #print(primes)
        for p in primes:
            if p % 4 == 1:
                self.answers.append(p)
        #print(answers)
        for v in self.answers[:len(self.answers)]:
            (p, i, r) = self.split_square(v)
            print(f'{p} = {i}^2 + {int(r)}^2')

def main():
    ''' main '''
    s = Solution()
    s.run()

if __name__ == '__main__':
    main()
