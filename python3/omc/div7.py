#!/usr/bin/env python3
# coding: utf-8
#

'''
s = 10^0 + 10^1 + 10^2 + ... + 10^98 + 10^99
s % 7 = ?
ans = 5
'''

def test() -> None:
    ''' test '''
    UPPER_LIMIT = 100
    total = 0
    print(f'{UPPER_LIMIT=}')
    for k in range(UPPER_LIMIT):
        r = pow(10, k, 7)    # 10 ** k % 7
        total += r
    print(total)
    print(total % 7)


def main() -> None:
    ''' main '''
    print(__doc__)
    test()

if __name__ == '__main__':
    main()
