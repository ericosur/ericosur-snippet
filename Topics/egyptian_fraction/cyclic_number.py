#!/usr/bin/env python3
# coding: utf-8

'''
This script is not for general purpose. Not all answers are optimized and correct.


* repeating decimal: https://mathworld.wolfram.com/RepeatingDecimal.html
* cyclic number https://mathworld.wolfram.com/CyclicNumber.html
* https://hr.userweb.mwn.de/numb/period.html

full reptend primes: 7, 17, 19, 23, 29, 47, 59, 61, 97... OEIS A001913

Examples of primes p such that the decimal period length of 1/p is (p-1)/K
k=3: 103, 127, 139, 331...

http://web.ntnu.edu.tw/~algo/Substring4.html
https://stackoverflow.com/questions/11090289/find-longest-repetitive-sequence-in-a-string
https://xlinux.nist.gov/dads/HTML/shortestCommonSuperstring.html
'''

import argparse
from lcs import longestRepeatedSubstring

class Cons:
    ''' use 2 to detect longest repeated substring '''
    multiple = 2

def stupid_div(p):
    ''' stupid divide '''
    if p < 3:
        print('[ERROR] need p >= 3')
        raise ValueError
    n = 1
    cnt = 0
    decs = []
    first = True
    while cnt < p*Cons.multiple:
        q = n // p
        r = n % p
        if first:
            first = False
        else:
            decs.append(q)
        n = r
        if n < p:
            n = n * 10
        cnt += 1

    # returns a list with digits of divide result,
    # eg: "[1,4,2,8,5,7]"
    return decs

def l2s(l):
    ''' l2s, join a integer list into a string '''
    a = [ str(x) for x in l ]
    s = ''.join(a)
    return s


def show(r):
    ''' show '''
    if not isinstance(r, list):
        print('[ERROR] should be a list')
        raise ValueError
    p = len(r) // Cons.multiple
    cnt = 0
    for c in r:
        if cnt and cnt%p==0:
            print()
        print(c,end='')
        cnt += 1
    print("\n")

def test(n):
    ''' test '''
    r = stupid_div(n)
    raw_digits = l2s(r)
    max_repeat = len(raw_digits)

    ans = []
    s = raw_digits
    lrs = ''
    cnt = 0
    while True:
        cnt += 1
        lrs = longestRepeatedSubstring(s)
        if len(lrs) <= 1:
            #print('[info] lrs is empty')
            break
        ans.append(lrs)
        s = lrs
        if cnt > max_repeat:
            print('too much?')
            break

    print(f'n = {n}: raw_digits: ({len(raw_digits)})')
    print(raw_digits)
    print('=' * 20 + ">")

    for a in ans:
        print('repeat:')
        print(a)
        print('len(s):')
        print(len(a))
        print('-' * 40)


'''
2*37   # l=3,135
7*31  # l=30,004608294930875576036866359447
7    # l=6,142857
23    # l=22,0434782608695652173913
37    # l=3,027
97
103
421   # 140
'''
def perform_test():
    ''' shoot tests '''
    test(7)
    test(2*37)
    test(7*31)

def proc(argv):
    ''' proc '''
    for a in argv:
        test(a)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    parser.add_argument("integers", metavar='ints', type=int, nargs='*', help="integers")
    parser.add_argument("-t", "--test", action='store_true', default=False,
        help='perform tests')

    args = parser.parse_args()

    if args.test:
        perform_test()
        return

    if len(args.integers) == 0:
        print('apply demo number...')
        args.integers.append(23)
    #print(args.integers)
    proc(args.integers)

if __name__ == '__main__':
    main()
