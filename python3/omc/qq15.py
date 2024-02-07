#!/usr/bin/python3
# coding: utf-8

'''
Q15, 今有任意5個自然數，計算其中任3個數的和，得到10個不同的自然數，它們是
15, 16, 18, 19, 21, 22, 23, 26, 27, 29, 這5個數的乘積是多少？
'''

import itertools as it


def main():
    ''' main test function '''

    UPPER = 15

    mm = list(range(1,UPPER))
    pp = list(range(1,UPPER))
    qq = list(range(1,UPPER))
    rr = list(range(1,UPPER))
    ss = list(range(1,UPPER))

    tries = []
    check_set = {17, 20, 24, 25, 28}

    for n in it.product(mm, pp, qq, rr, ss):
        if len(set(n)) != 5:
            continue
        the_list = list(n)
        list_sums = set()
        for v in it.combinations(the_list, 3):
            t = sum(list(v))
            if 15<=t<=29:
                if t not in check_set:
                    list_sums.add(t)
        if len(list_sums) == 10:
            print(n, list_sums)


if __name__ == '__main__':
    main()
