#!/usr/bin/env python3
# coding: utf-8

'''
Use method Sieve of Eratosthenes to collect primes up to self.upper
refer to: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

import bisect
import math
import time

class SieveOfEratosthenes():
    ''' implement '''
    def __init__(self):
        self.prime = 3
        self.upper = 1000000
        self.target = [2]
        self.last_prime = 0
        self.init_target()
        # if upper limit is 100, only need to check prime factor to sqrt(100)
        self.inner_limit = math.sqrt(self.upper-1)

    def __str__(self):
        r = f'SieveOfEratosthenes: from 2 to {self.upper}'
        return r

    def init_target(self):
        ''' init target list, here skip all even numbers '''
        #start_time = time.time()
        v = 3
        while v <= self.upper:
            self.target.append(v)
            v += 2
        #print('== took:{:.2f}'.format(time.time() - start_time))

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
        ''' filter specified prime from target '''
        start_time = time.time()
        if self.last_prime == p:
            return
        for t in self.target:
            if t > p and t % p == 0:
                try:
                    # list.remove() is easy but slow esp. list is large
                    #self.target.remove(t)
                    # use get_bisect() to locate position of element
                    i = SieveOfEratosthenes.get_bisect(self.target, t)
                    # list.pop() is O(1)
                    self.target.pop(i)
                except ValueError:
                    pass
        d = time.time() - start_time
        if d > 1.0:
            print(f'>>>>>> start filter {p} len: {len(self.target)}')
            print(f'<<<<<< took:{d:.2f}: end filter')

    def run_filter(self):
        ''' filter primes from target '''
        pp = self.prime
        #print('=====> pp: {}'.format(pp))

        if pp != self.last_prime:
            self.filter_prime(pp)
            self.last_prime = pp
        else:
            print('skip')
            return

        if pp > self.inner_limit:
            print('hit inner limit')
            return

        #start_time = time.time()
        ii = 0
        k = self.target[ii]
        #print(self.target)
        while k <= self.last_prime:
            ii += 1
            k = self.target[ii]
            self.prime = k
        #print('***** took:{:.2f}'.format(time.time() - start_time))
        self.run_filter()


    def run(self):
        ''' run '''
        self.run_filter()

    def get_target(self):
        ''' get left numbers '''
        return self.target

    @staticmethod
    def output_to_file(fn, primes):
        ''' output list into text file '''
        with open(fn, "wt", encoding='utf8') as ofh:
            for pp in primes:
                ofh.write(f"{pp}\n")
        print(f'output to {fn}, count = {len(primes)}')


def main():
    ''' main '''
    soe = SieveOfEratosthenes()
    print(soe)
    soe.run()
    r = soe.get_target()
    print('len of result:', len(r))
    if len(r) < 199:
        print('result:', r)

    # uncomment the following line if output to file
    # use 'check_need.py to check if every number is prime'
    soe.output_to_file('need_check.txt', r)


if __name__ == '__main__':
    main()
