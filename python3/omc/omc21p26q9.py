#!/usr/bin/env python3
# coding: utf-8

'''
P(2/6) Q9. 芷萱 14,18,22,26; 佳忻 16,22,28,34
請問500以內，她們兩人所寫相同的數總和是多少？
'''


def main():
    ''' main '''
    upper = 500
    p = set(range(14, upper+1, 4))
    q = set(range(16, upper+1, 6))
    x = p.intersection(q)
    sortx = list(x)
    sortx.sort()
    print(sortx)
    print(sum(sortx))


if __name__ == '__main__':
    main()
