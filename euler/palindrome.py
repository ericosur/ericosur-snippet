#!/usr/bin/env python3
# coding: utf-8

'''
http://projecteuler.net/problem=4
http://en.wikipedia.org/wiki/Palindromic_number
http://www.csie.ntnu.edu.tw/~u91029/Palindrome.html

zh: 回文數

palindromic primes
https://oeis.org/A002385

'''

import itertools as it
import numpy as np

def is_palindrome(s):
    '''
    [in] s: numeric string
    return True/False if palindrome number
    '''
    chs = list(s)   # chs is list of each char of s
    lns = len(s)
    for i, cc in enumerate(chs):
        if cc != chs[lns - 1 - i]:
            return False
    return True


def main():
    ''' main '''
    result = []
    mymax = 1
    cnt = 0
    pp = range(999, 800, -1)
    qq = range(999, 800, -1)
    # use itertools to create one-level-depth instead of two-level nested loop
    for nn in it.product(pp, qq):
        cnt += 1
        multi = np.prod(nn)
        if multi < mymax:
            break
        if is_palindrome(str(multi)):
            result.append(multi)
            if multi > mymax:
                mymax = multi
                print('{} = {} x {}'.format(multi, nn[0], nn[1]))
                break

    print("after test", cnt, "numbers to get max palindrome")
    print("my max", mymax)
    print("max palindrome is", max(result))


if __name__ == '__main__':
    main()
