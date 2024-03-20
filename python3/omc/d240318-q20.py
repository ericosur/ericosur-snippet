#!/usr/bin/env python3
# coding: utf-8
#

'''
Q20. 已知n是最小的自然數使得7n剛好是一個2021位數，求n的個位數字
'''

import sympy


def main() -> None:
    ''' main '''
    print(__doc__)
    k = 2020
    r = pow(10, k, 7)    # 10 ** k % 7
    print(f'10**2020 mod 7 = {r}')


if __name__ == '__main__':
    main()
