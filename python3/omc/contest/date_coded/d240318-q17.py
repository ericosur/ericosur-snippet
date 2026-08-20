#!/usr/bin/env python3
#

'''
Q17. 求最小的正整數n使得4n-1與4n+1都不是質數
'''

from sympy import ntheory


def isprime(n):
    ''' is a prime '''
    return ntheory.isprime(n)

def main() -> None:
    ''' main '''
    print(__doc__)
    for n in range(1,99+1):
        p = 4*n-1
        q = 4*n+1
        if not isprime(p) and not isprime(q):
            print(n, p, q)


if __name__ == '__main__':
    main()
