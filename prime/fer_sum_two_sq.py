#!/usr/bin/python3
# coding: utf-8
#

'''
Fermat's theorem on sums of two squares

ref: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares

'''

import sys

try:
    # larger and slower
    from store import LoadCompressPrime as StorePrime
    print('use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker
    from store import StorePrime
    print('use **store_prime**')

# pylint: disable=invalid-name
class Solution():
    ''' it is similar to goldbach conf? '''

    UPPER_BOUND = 99999
    LOWER_BOUND = 3

    def __init__(self):
        self.sp = StorePrime()
        # self.sp.load

    # def is_prime(self, n):
    #     ''' is a prime ? '''
    #     ret = self.sp.find(n)
    #     return ret is not None

    @staticmethod
    def is_quadratic(n):
        ''' check if meets p = 4k + 1 '''
        return (n % 4) == 1

    def run(self):
        ''' run this '''
        tests = [97, 37, 41]
        for p in tests:
            ret = self.sp.get_primes_less_than(p)
            if ret is not None:
                print(p)

def main():
    ''' main '''
    print('it is a unfinished scripts')
    sys.exit(1)
    # solution = Solution()
    # solution.run()

if __name__ == '__main__':
    main()
