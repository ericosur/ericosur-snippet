#!/usr/bin/env python
'''
to find P, which satisfy:
    P = m ** 2 + n ** 2
    P is a prime and P < 10000
    m and n are primes as well

reference from http://www.cg45.cn/archives/246
It is a missing link. Maybe related to Fermat's theorem on sums of two squares.

NOTE: also refer to sqare_root.py, which using miller robin method to test prime number

'''

from math import sqrt
import sys
from load_myutil import GetConfig
from store_prime import StorePrime

try:
    from sympy import ntheory
except ImportError as err:
    print('[FAIL] cannot import sympy')
    sys.exit(-1)

MODNAME = "RootSquares"
RUN_TEST_ONLY = False

def is_prime_nth(n: int):
    ''' check if a prime with sympy '''
    return ntheory.primetest.isprime(n)

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3f} sec')

class Solution():
    ''' to find certain P '''
    UPPER_BOUND = 10000
    LOWER_BOUND = 3

    def __init__(self):
        self.results = []

        obj = GetConfig()
        obj.set_configkey("small")
        txtfn = obj.get_full_path("txt")
        pfn = obj.get_full_path("pickle")
        self.sp = StorePrime(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()

    def get_results(self):
        ''' get resutls '''
        return self.results

    def in_upperbound(self, val):
        ''' true if val is in the bound '''
        return val <= self.sp.get_maxprime()

    def is_prime2(self, val):
        ''' is a prime version with StorePrime '''
        (p, q) = self.sp.get_around(val)
        if p and q is None:
            return True
        return False

    def is_prime(self, val):
        ''' is a prime version with StorePrime '''
        try:
            i = self.sp.find(val)
            return 0 <= i < self.sp.get_count()
        except ValueError:
            return False

    def run_loop(self, check_func):
        ''' run loop
            m, n, P are primes,
            only n = 2 would make P odd because m and m*m are odd
        '''
        L = self.LOWER_BOUND
        U = int(sqrt(self.UPPER_BOUND))
        results = []
        for m in range(L, U, 2):
            if not self.in_upperbound(m):
                print(f'{m} is OOB, skip')
                continue
            if check_func(m):
                p = m**2 + 4
                if not self.in_upperbound(p):
                    print(f'{p} is OOB, skip')
                    continue
                if check_func(p):
                    results.append((m, p))
        return results

    def action(self) -> None:
        ''' action 3 run loops '''
        r = self.run_loop(self.is_prime)
        self.show_results(r)
        # r = self.run_loop(self.is_prime2)
        # self.show_results(r)
        # r = self.run_loop(is_prime_nth)
        # self.show_results(r)

    def show_results(self, res):
        ''' show results '''
        print(f"From {self.LOWER_BOUND} to {self.UPPER_BOUND} ==>")
        print(f'get {len(res)} results')
        for (m, p) in res:
            print(f'{p:8d} = {m:4d}^2 + 2^2')

    def test_self(self):
        ''' run test '''
        for i in range(2, 100):
            if self.is_prime(i):
                print(f'{i} is a prime')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()

        if RUN_TEST_ONLY:
            obj.test_self()
            return

        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
