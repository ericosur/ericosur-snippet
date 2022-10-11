#!/usr/bin/python3
# coding: utf-8
#

'''
Fermat's theorem on sums of two squares

ref: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares

'''

from random import randint

try:
    # larger and slower
    from sip import LoadCompressPrime as StorePrime
    print('use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker
    from store_prime import StorePrime
    print('use **store_prime**')

class Solution():
    ''' it is similar to goldbach conf? '''

    UPPER_BOUND = 99999
    LOWER_BOUND = 3

    def __init__(self):
        pass


    def is_prime(self, n):
        ''' is a prime ? '''
        ret = self.sp.find(n)
        return ret is not None

    @staticmethod
    def is_quadratic(n):
        ''' check if meets p = 4k + 1 '''
        return (n % 4) == 1

    @staticmethod
    def run():
        ''' run this '''
        tests = [97, 37, 41]
        with StorePrime() as sp:
            for p in tests:
                ret = sp.get_primes_less_than(p)
                if ret is not None:
                    print(p)

def main():
    ''' main '''
    #solution = Solution()
    Solution.run()

if __name__ == '__main__':
    main()
