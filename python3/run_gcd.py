#!/usr/bin/env python3
# coding: utf-8

'''
simple gcd runner with argparse

here benchmark:
    - local_gcd
    - math_gcd
    - numpy_gcd

'''

import argparse

# official math.gcd
from math import gcd as math_gcd
from random import randint
from timeit import timeit
try:
    from numpy import gcd as numpy_gcd
    USE_NUMPY = True
except ImportError:
    USE_NUMPY = False
    numpy_gcd = None
# local implementation of gcd
from the_gcd import gcd as local_gcd

DEFAULT_NUMBER = 1_000_000

def dont_duplicate(m):
    ''' get a random number different from m '''
    n = randint(101, 999_999)
    while n == m:
        n = randint(101, 999_999)
    return n

def test1():
    ''' test1 w/ local gcd '''
    m = randint(101, 999_999)
    n = dont_duplicate(m)
    local_gcd(m, n)

def test2():
    ''' test2 w/ math.gcd '''
    m = randint(101, 999_999)
    n = dont_duplicate(m)
    math_gcd(m, n)

def test3() -> set:
    ''' test3 w/ numpy.gcd
        Note:
        - It will be slower than local_gcd if call numpy.gcd with one pair of
          scalar numbers.
        - If I prepare two np.ndarray with 1_000_000 elements, and call
          numpy.gcd once. It could be faster.
    '''
    if not USE_NUMPY:
        print('numpy not available')
        return set()

    ans = set()
    m_list = []
    n_list = []
    for _ in range(DEFAULT_NUMBER):
        m = randint(101, 999_999)
        n = dont_duplicate(m)
        m_list.append(m)
        n_list.append(n)
    r = numpy_gcd(m_list, n_list)
    ans.add(tuple(r))
    return ans

def run_demo():
    ''' run demo '''
    print('DEMO mode: run gcd(1024, 768)')

    r1 = timeit("test1()", setup='from __main__ import test1', number=DEFAULT_NUMBER)
    #print(f'len: {len(ans)}')
    print(f'local_gcd: {r1}')
    r2 = timeit("test2()", setup='from __main__ import test2', number=DEFAULT_NUMBER)
    #print(f'len: {len(ans)}')
    print(f'math_gcd: {r2}')
    r3 = timeit("test3()", setup='from __main__ import test3', number=1)
    #print(f'len: {len(ans)}')
    print(f'num_gcd: {r3}')

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='calculate Greatest Common Divisor')
    parser.add_argument("n1", type=int, nargs='?', default=1024)
    parser.add_argument("n2", type=int, nargs='?', default=768)
    parser.add_argument("--demo", action='store_true', default=False, help='apply demo mode')
    args = parser.parse_args()

    if args.demo:
        run_demo()
        return

    r = local_gcd(args.n1, args.n2)
    print(f'gcd({args.n1}, {args.n2}) = {r}')

if __name__ == '__main__':
    main()
