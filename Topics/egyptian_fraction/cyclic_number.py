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

'''

'''
http://web.ntnu.edu.tw/~algo/Substring4.html
https://stackoverflow.com/questions/11090289/find-longest-repetitive-sequence-in-a-string
https://xlinux.nist.gov/dads/HTML/shortestCommonSuperstring.html
'''

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
    decs = list()
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
    print('n =', n)
    r = stupid_div(n)
    raw_digits = l2s(r)
    max_repeat = len(raw_digits)

    s = raw_digits
    lrs = ''
    cnt = 0
    while True:
        cnt += 1
        lrs = longestRepeatedSubstring(s)
        if len(lrs) <= 1:
            print('[info] lrs is empty')
            break
        s = lrs
        if cnt > max_repeat:
            print('too much?')
            break
    print('raw_digits:')
    print(raw_digits)

    print('repeat:')
    print(s)
    print('len(s):')
    print(len(s))
    print('-' * 40)


def main():
    ''' main '''
    #test(7)
    #test(97)
    # test(103)
    # test(421)
    #test(23)
    test(421)

if __name__ == '__main__':
    main()
