#!/usr/bin/python3
# coding: utf-8

'''
Pythagorean triple

a^2 + b^2 = c^2, and a, b, c are coprime

Here I use two methods to search pythagorean triple numbers.
Method 1:
    try if the 3rd number is integer

Method 2:
    m, n are positive integers, m > n,
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2
    if gcd(m, n) == 1, (m, n) is one odd, one even

reference:
    * https://en.wikipedia.org/wiki/Special_right_triangle
    * https://en.wikipedia.org/wiki/Pythagorean_triple

'''

import math
import itertools as it
import time

import numpy as np

class Pythag():
    ''' class to find pythagorean triples '''
    def __init__(self):
        self.mnlist = []
        # all three numbers in tuple should smaller than max_num
        self.max_num = 1000

        # it will slow down if using np.gcd, maybe I cannot benifit from
        # external function call with small mount data. Mostly, I could expect
        # numpy functions quicker than internal function
        #
        #self.gcd = np.gcd    # numpy.gcd
        self.gcd = self._gcd  # local gcd function

    @staticmethod
    def _gcd(m: int, n: int) -> int:
        '''
        calculate gcd number by rescursive
        '''
        if n == 0:
            return m
        return Pythag._gcd(n, m % n)

    @staticmethod
    def sqrt_sum(a, b) -> float:
        ''' sum '''
        return math.sqrt(a*a + b*b)

    @staticmethod
    def get_dist(a, b) -> float:
        ''' use numpy to get distance '''
        m = np.array([a, b])
        d = np.linalg.norm(m)
        return d

    @staticmethod
    def show_list(tripes: list) -> None:
        ''' show list of tuples '''
        COLS = 5
        cnt = 0
        for t in tripes:
            if cnt != 0 and cnt % COLS == 0:
                print()
            print(t, end=' ')
            cnt += 1
        print()

    def method1(self):
        ''' test '''
        a1 = []
        cnt = 0
        for (m, n) in it.combinations(range(1, self.max_num), 2):
            cnt += 1
            if self.gcd(m, n) != 1:  # m, n are not coprime
                continue

            r = self.sqrt_sum(m, n)
            if r >= self.max_num:
                continue

            if math.floor(r) == math.ceil(r):
                a1.append((m, n, int(r)))

        print('cnt:', cnt)
        return a1

    @staticmethod
    def mn2tri(m, n):
        ''' mn2tri '''
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        return (a, b, c)

    def get_mnlist(self):
        ''' find m, n list '''
        self.mnlist = []
        cnt = 0
        # will get 11, 12, 13, ..., 21, 22, 23, ...
        for (m, n) in it.product(range(1, self.max_num), repeat=2):
            cnt += 1

            if m <= n:
                #print(f'{m} <= {n}')
                continue
            if self.gcd(m, n) == 1:
                #print(f'gcd({m}, {n}) == 1')
                if (m+n)%2 == 1:
                    self.mnlist.append((m, n))

        print('len of mnlist:', len(self.mnlist))
        print('cnt:', cnt)
        #self.show_list(self.mnlist)

    def get_tripes(self):
        ''' get triples '''
        res = []
        for (m, n) in self.mnlist:
            (a, b, c) = self.mn2tri(m, n)
            if a > self.max_num:
                continue
            if b > self.max_num:
                continue
            if c > self.max_num:
                continue
            if a > b:
                a, b = b, a
            res.append((a, b, c))
        return res

    def method2(self):
        ''' m, n are positive integers, m > n,
            a = m^2 - n^2
            b = 2mn
            c = m^2 + n^2
            if gcd(m, n) == 1, (m, n) is one odd, one even
        '''
        self.get_mnlist()
        res = self.get_tripes()
        return res


    @staticmethod
    def sort_and_output(tripes: list, fn: str) -> None:
        ''' sort the list and output to file '''
        result_list = sorted(tripes, key=lambda x: (x[0], x[1], x[2]))
        print('length:', len(result_list))
        ''' output results to specified file '''
        with open(fn, "wt", encoding='utf-8') as fobj:
            for t in result_list:
                print(t, file=fobj)
        print(f'output {len(result_list)} elements to {fn}')


    def action(self) -> None:
        ''' trigger this '''
        start = time.time()
        r1 = self.method1()
        d1 = time.time() - start
        self.sort_and_output(r1, "r1.txt")

        start = time.time()
        r2 = self.method2()
        d2 = time.time() - start
        self.sort_and_output(r2, "r2.txt")

        print(f'all elements are smaller than {self.max_num}')
        print(f'time duration: d1={d1:.4f}, d2={d2:.4f}')

def main():
    ''' main '''
    tri = Pythag()
    tri.action()

if __name__ == '__main__':
    main()
