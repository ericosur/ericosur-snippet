#!/usr/bin/python3
# coding: utf-8

'''
43  1   67
61  37  13
7   73  31

67  1   43
13  37  61
31  73  7


5 is 6*1-1
7 is 6*1+1
11 is 6*2-1
13 is 6*2+1
17 is 6*3-1
19 is 6*3+1
23 is 6*4-1
29 is 6*5-1
31 is 6*5+1
37 is 6*6+1
41 is 6*7-1
43 is 6*7+1
47 is 6*8-1
53 is 6*9-1
59 is 6*10-1
61 is 6*10+1
67 is 6*11+1
71 is 6*12-1
73 is 6*12+1
79 is 6*13+1
83 is 6*14-1
89 is 6*15-1
97 is 6*16+1

'''

import sys

try:
    #from sympy import sympy.ntheory.primetest.isprime
    from sympy import ntheory
except ImportError as err:
    print('Import Error while:', err)
    sys.exit(1)

class Solution():
    def __init__(self):
        self.primes = []
        self.init_primes()

    @staticmethod
    def is_prime(n):
        return ntheory.primetest.isprime(n)

    def init_primes(self):
        for i in range(1,100):
            if self.is_prime(i):
                self.primes.append(i)

    def dump(self):
        print(self.primes)

    def run(self):
        for p in self.primes:
            if p % 6 == 1:
                q = int(p / 6)
                print(f'{p} is 6*{q}+1')
            elif p % 6 == 5:
                q = int(p / 6) + 1
                print(f'{p} is 6*{q}-1')


def main():
    ''' main '''
    print('main')
    sol = Solution()
    sol.run()

if __name__ == '__main__':
    main()
