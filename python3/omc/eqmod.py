#!/usr/bin/env python3
# coding: utf-8
#

'''
31513
34369
'''

def test() -> None:
    ''' test '''
    m = 31513
    n = 34369
    for k in range(100,1000):
        p = m % k
        q = n % k
        if p == q:
            print(k, p, q)


def main() -> None:
    ''' main '''
    print(__doc__)
    test()

if __name__ == '__main__':
    main()
