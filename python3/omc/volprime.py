#!/usr/bin/python3

'''
0, 1, 2, 3
three-digit number is prime
'''

from sympy import ntheory


def is_prime(n):
    ''' true if n is a prime number '''
    return ntheory.primetest.isprime(n)

def test_prime():
    ''' test_prime '''
    vals = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,49]
    for n in vals:
        if is_prime(n):
            print(f'{n} is prime')

def main():
    ''' main '''
    print('main')
    test_prime()

if __name__ == '__main__':
    main()
