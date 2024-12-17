#!/usr/bin/env python3
# coding: utf-8

'''
Use method Sieve of Eratosthenes to collect primes up to self.upper
refer to: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

import bisect
import math
from time import time

from store import GetConfig
from store import StorePrime as sp
from store import prt

MODNAME = "sieve.py"
def show_duration(duration):
    ''' show duration '''
    prt(f'{MODNAME}: duration: {duration:.3f} sec')

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("small")    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    return txtfn, pfn

class SieveOfEratosthenes():
    ''' implement '''
    upper = 1_000_000
    REPEAT = 20

    def __init__(self):
        self.prime = 3
        self.results = [2]
        self.last_prime = 0
        self.init_target()
        # if upper limit is 100, only need to check prime factor to sqrt(100)
        self.inner_limit = math.sqrt(self.upper-1)

        self.sp = None
        self.ok_to_verify = self._check()

    def __str__(self):
        r = f'SieveOfEratosthenes: from 2 to {self.upper:,}'
        return r

    def _check(self):
        ''' check if ok to use StorePrime to validate results '''
        txtfn, pfn = wrap_config()
        self.sp = sp(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()
        _max = self.sp.at(self.sp.get_count() - 1)
        if self.upper > _max:
            prt("[WARN] stored primes are not large enough to validate the results")
            del self.sp
            self.sp = None
            return False
        return True

    def init_target(self):
        ''' init list, here skip all even numbers '''
        v = 3
        while v <= self.upper:
            self.results.append(v)
            v += 2

    def get_result(self):
        ''' get left numbers '''
        return self.results

    @staticmethod
    def get_bisect(a, x):
        '''
        Locate the leftmost value exactly equal to value **x** from list **a**
        return index if x is in the list
        raise ValueError if not exist
        it will be faster than **if x in a** or __a.remove(x)__
        '''
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    def filter_prime(self, p):
        ''' filter specified prime from results '''
        start = time()
        if self.last_prime == p:
            return
        for t in self.results:
            if t > p and t % p == 0:
                try:
                    # list.remove() is easy but slow esp. list is large
                    #self.target.remove(t)
                    # use get_bisect() to locate position of element
                    i = SieveOfEratosthenes.get_bisect(self.results, t)
                    # list.pop() is O(1)
                    self.results.pop(i)
                except ValueError:
                    pass
        d = time() - start
        if d > 0.75:
            prt(f'>>>>>> start filter {p} len: {len(self.results):,}')
            prt(f'<<<<<< took:{d:.3f} sec')

    def run_filter(self):
        ''' filter primes from target '''
        pp = self.prime
        #prt(f'=====> pp: {pp}')

        if pp != self.last_prime:
            self.filter_prime(pp)
            self.last_prime = pp
        else:
            prt('skip')
            return

        if pp > self.inner_limit:
            prt('hit inner limit')
            return

        ii = 0
        k = self.results[ii]
        #prt(self.target)
        while k <= self.last_prime:
            ii += 1
            k = self.results[ii]
            self.prime = k
        self.run_filter()

    def verify_result(self):
        ''' verify result '''
        if not self.ok_to_verify:
            prt("[FAIL] cannot use stored primes to validate")
            return
        l = len(self.results)
        prt(f'verify_result: len of results: {l:,}')
        stored_primes = self.sp.get_primes_less_than(self.results[-1]+1)
        prt(f'verify_result: fetched stored primes: {len(stored_primes):,}')
        if stored_primes == self.results:
            prt('verify_result: matched')
        else:
            prt('verify_result: not matched')

    def output_to_file(self, fn):
        ''' output into text file '''
        with open(fn, "wt", encoding='utf8') as ofh:
            for p in self.results:
                prt(p, file=ofh)
        prt(f'[INFO] sieve.py: output to {fn}, count = {len(self.results):,}')

    def action(self):
        ''' run '''
        self.run_filter()

    def show_result(self):
        ''' show '''
        r = self.results
        prt('len of results:', len(r))
        if len(r) < self.REPEAT:
            prt('all result:', r)
        else:
            m = len(r) // 2
            the_lower = m - self.REPEAT // 2
            the_upper = m + self.REPEAT // 2
            s = slice(the_lower, the_upper)
            prt(f"some prime numbers from the result from {the_lower}..{the_upper}")
            prt(r[s])
            # uncomment the following line if output to file
            # use 'check_need.py to check if every number is prime'
            #obj.output_to_file('sieve_primes.txt')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        prt(obj)
        start = time()
        obj.action()
        duration = time() - start
        obj.show_result()
        obj.verify_result()
        show_duration(duration)

def main():
    ''' main '''
    SieveOfEratosthenes.run()

if __name__ == '__main__':
    main()
