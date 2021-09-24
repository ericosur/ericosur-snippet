#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
algorithm of __Sieve of Eratosthenes__
wiki: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
and reference: http://www.csie.ntnu.edu.tw/~u91029/SieveOfEratosthenes.html

Prime Sieve of Eratosthenes
http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes
'''

from __future__ import print_function
import math

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
    #   print("#", g_count, arr)
    #   print("prime.append(%d", arr[0])
        # the first one is prime
        self.primes.append(self.arr[0])

        pp = self.arr[0]
        inc = self.arr[0]

        while pp <= self.arr[-1]:
            if self.arr.__contains__(pp):
                self.arr.remove(pp)  # remove the multiples
                #print(pp, " removed")
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

    def run(self):
        ''' run me to do sieve '''
        self.fill_array()
        self.del_elem()



def main():
    '''main function'''
    MAX_NUMBER = 1000
    sieve_obj = Sieve(MAX_NUMBER)
    sieve_obj.run()

    print(f'# filter primes from 1 to {MAX_NUMBER}')
    print(f"# total pass: {sieve_obj.get_count()}" )
    primes = sieve_obj.get_primes()
    print(f"# found {len(primes)} primes")

    for pr in primes:
        print(pr)


if __name__ == "__main__":
    main()
