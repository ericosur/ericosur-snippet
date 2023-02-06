#!/usr/bin/python3
# coding: utf-8

'''
(1,5,10,50)
(3,3,2,1)
'''

import numpy as np
import itertools as it

def main():
    ''' main '''
    c = [50, 10, 5, 1]

    pp = list(range(2))
    qq = list(range(3))
    rr = list(range(4))
    ss = list(range(4))

    ans = {}
    cnt = 0
    for x in it.product(pp, qq, rr, ss):
        v = np.dot(c, x)
        if v == 0:
            continue
        cnt += 1
        print(c, x, v)
        ans[v] = 1

    print('cnt:', cnt)
    print(len(ans.keys()))

if __name__ == '__main__':
    main()
