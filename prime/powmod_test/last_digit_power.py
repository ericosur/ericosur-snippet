#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
題目：
計算 4001 的 5003 次方的未四位數

解答：
在許多場合直接計算會overflow，而問題只要末四位數，所以只取
10000以下的數字作運算即可，也不會overflow，在32bit下，此招
可以用到46340的若干次方

此計算相當於 4001^5003 mod 10000 的結果

4003**5003 有 41497 個數字 5003 * log10(4007) (無條件進入整數)


```math
4001^{5003} mod 10000
```

There is a built-in function **pow** in python.

'''

import sys
from powers_modulo import powmod

def calc(base: int, radix: int):
    '''calc'''
    n = 10000
    m = powmod(base, radix, n)
    print("%d ** %d 的末四位數: %d" % (base, radix, m))
    assert m == pow(base, radix, n)

def main(argv):
    ''' main '''
    v = []
    try:
        for i in argv:
            v.append(int(i))
    except ValueError:
        print('value error at {}'.format(i))

    calc(v[0], v[1])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('demo mode')
        main([4381, 5003])
    else:
        main(sys.argv[1:])
