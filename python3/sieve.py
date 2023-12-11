#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
algorithm of __Sieve of Eratosthenes__
wiki: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
and reference: http://www.csie.ntnu.edu.tw/~u91029/SieveOfEratosthenes.html

Prime Sieve of Eratosthenes
http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes

tag: prime number
'''

from __future__ import print_function

import math

HAS_SYMPY = False

try:
    from sympy import ntheory
    HAS_SYMPY = True
except ImportError as err:
    print('Import Error while:', err)


class Sieve():
    ''' class Sieve demos "Prime Sieve of Eratosthenes" '''

    def __init__(self, max_number):
        self.arr = []
        self.arr_max = max_number
        self.g_count = 0
        self.primes = [2]

    def fill_array(self):
        '''
            even numbers would not be filled in this array
        '''
        i = 3
        while i <= self.arr_max:
            self.arr.append(i)
            i += 2

    def fill_array_old(self):
        '''
            fill array from 2 to arr_max-1
        '''
        for i in range(2, self.arr_max):
            self.arr.append(i)

    def del_elem(self):
        ''' remove multiple values from array '''
        self.g_count += 1
        # print("#", g_count, arr)
        # print("prime.append(%d", arr[0])
        # the first one is prime
        self.primes.append(self.arr[0])

        pp = self.arr[0]
        inc = self.arr[0]

        while pp <= self.arr[-1]:
            # Unnecessarily calls dunder method __contains__
            # Use in keyword
            # if self.arr.__contains__(pp):
            if pp in self.arr:
                self.arr.remove(pp)
            pp += inc           # next multiple

        if self.arr[0] > math.sqrt(self.arr_max):
            # print("%d > %f" % (arr[0], math.sqrt(arr_max)))
            if self.arr:
                for bb in self.arr:
                    self.primes.append(bb)
            return
        self.del_elem()

    def get_count(self):
        ''' return number of pass '''
        return self.g_count

    def get_primes(self):
        ''' return remaining primes '''
        return self.primes


    @classmethod
    def run(cls, max_number):
        ''' run me to do sieve '''
        obj = cls(max_number)
        obj.fill_array()
        obj.del_elem()
        return obj


def main():
    '''main function'''

    # function name alias
    is_prime = None
    if HAS_SYMPY:
        is_prime = ntheory.primetest.isprime

    MAX_NUMBER = 3_000
    sieve_obj = Sieve.run(MAX_NUMBER)

    print(f'# filter primes from 1 to {MAX_NUMBER}')
    print(f"# total pass: {sieve_obj.get_count()}" )
    primes = sieve_obj.get_primes()
    print(f"# found {len(primes)} primes")

    for n in primes:
        # double confirm via sympy function
        if is_prime and not is_prime(n):
            print('[error] {n} is not a prime number !!')
        print(n, end=' ')
    print()


if __name__ == "__main__":
    main()
