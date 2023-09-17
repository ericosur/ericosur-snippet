#!/usr/bin/env python3
# coding: utf-8
#

'''
if square number is odd, its remainder is 1 after modulus 8
test() will check this
'''

def test() -> None:
    ''' test '''
    print(pow(56,56,13))

def is_valid(n):
    primes = [3,5,7,11,13]
    for p in primes:
        if n % p != 2:
            return False
    return True

def test2():
    primes = [3,5,7,11,13]
    for i in range(3,200000):
        if is_valid(i):
            print(i)
            break


def main() -> None:
    ''' main '''
    print(__doc__)
    test2()

if __name__ == '__main__':
    main()
