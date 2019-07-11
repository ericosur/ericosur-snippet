# -*- coding: utf-8 -*-
"""
@author: neo
http://projecteuler.net/problem=40
"""

import numpy as np

def main():
    '''main'''
    d = ''
    i = 1
    upper = 1000002
    while len(d) < upper:
        d = d + str(i)
        i += 1

    # a list of str
    watched = [d[0], d[9], d[99], d[999], d[9999], d[99999], d[999999]]
    # map into a list of int
    val = list(map(int, watched[:]))
    ans = np.prod(val)
    print('ans:', ans)

if __name__ == '__main__':
    main()
