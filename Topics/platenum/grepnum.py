#!/usr/bin/env python
#

from itertools import product
from math import sqrt

# v is tuple
def checkIfPerfectSquare(tup, needPrintOut=False):
    int1,int2,int3,int4 = tup
    val = int1*1000 + int2*100 + int3*10 + int4
    m = int(sqrt(val))
    result = (val - m * m == 0)
    if result and needPrintOut:
        print("| {0} | {1} |".format(val, m))
    return result


def checkAllNumbers():
    #of = 'allnums.txt'

    # there is no digit 4
    nums = [0, 1, 2, 3, 5, 6, 7, 8, 9]
    itrs = product(nums, repeat=4)

    #with open(of, "w") as text_file:
    cnt = 0
    perfect_list = []
    for cc in itrs:
        #text_file.write(str(cc) + '\n')
        if cc[0] == 0:
            continue
        if checkIfPerfectSquare(cc, True):
            cnt = cnt + 1
            perfect_list.append(cc)
    print("There are {0} perfect squares".format(cnt))
    #print("size:{0}".format(len(perfect_list)))

if __name__ == '__main__':
    checkAllNumbers()
