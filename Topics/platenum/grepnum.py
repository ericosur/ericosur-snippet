#!/usr/bin/env python3
# coding: utf-8

''' check perfect square numbers '''

from itertools import product
from math import sqrt

def list_to_integer(digits: tuple) -> int:
    ''' list to integer
        (1, 2, 3, 4) will be int(1234)
    '''
    v = list(digits).copy()
    v.reverse()
    s = 0
    t = 1
    for x in v:
        s = s + int(x) * t
        t = t * 10
    return s

# v is tuple
def is_perfect_square(tup, needPrintOut=False):
    ''' is_perfect_square '''
    val = list_to_integer(tup)
    m = int(sqrt(val))
    result = (val - m * m == 0)
    if result and needPrintOut:
        print("| {0} | {1} |".format(val, m))
    return result


def check_all_numbers():
    ''' check_all_numbers '''
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
        if is_perfect_square(cc, True):
            cnt = cnt + 1
            perfect_list.append(cc)
    print("There are {0} perfect squares".format(cnt))
    #print("size:{0}".format(len(perfect_list)))

if __name__ == '__main__':
    check_all_numbers()
