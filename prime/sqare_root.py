#!/usr/bin/env python
'''
to find P, which satisfy:
    P = m ** 2 + n ** 2
    P is a prime and P < 10000
    m and n are primes as well

reference from http://www.cg45.cn/archives/246
It is a missing link. Maybe related to Fermat's theorem on sums of two squares.
'''

from math import sqrt
from MillerRabin import miller_rabin

class Solution():
    ''' to find certain P '''
    UPPER_BOUND = 99999
    LOWER_BOUND = 3

    def __init__(self):
        self.results = []

    @staticmethod
    def is_prime(nn):
        '''
            a wrapper function of miller_rabin()
        '''
        return miller_rabin(nn)

    def get_results(self):
        ''' get resutls '''
        return self.results

    def run(self) -> None:
        '''
            m, n, P are primes,
            only n = 2 would make P odd because m and m*m are odd
        '''
        L = self.LOWER_BOUND
        U = int(sqrt(self.UPPER_BOUND))

        for m in range(L, U, 2):
            if self.is_prime(m):
                p = m**2 + 4
                if self.is_prime(p):
                    self.results.append((m, p))



def main():
    ''' main '''
    find_solution = Solution()
    find_solution.run()

    res = find_solution.get_results()
    print(f"From {find_solution.LOWER_BOUND} to {find_solution.UPPER_BOUND} ==>")
    print(f'get {len(res)} results')
    for (m, p) in res:
        print(f'{p:8d} = {m:4d}^2 + 2^2')


if __name__ == '__main__':
    main()
