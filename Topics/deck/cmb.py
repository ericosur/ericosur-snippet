#!/usr/bin/env python

'''
In the game '17 pokers', combinations could be described as
C(17, 5). This script uses ''itertools.combinations'' to list
all possible combination.
'''
from itertools import combinations

print_to_stdout = 0

def output_list_to_file(output_file, cclist):
    with  open(output_file, "w") as text_file:
        cnt = 0
        for cc in cclist:
            if print_to_stdout:
               print cc
            text_file.write(str(cc)+'\n')
            cnt = cnt + 1

    print("output to file {0}, total {1} items".format(output_file, cnt))


if __name__ == '__main__':
    output_file = 'all-cmb.txt'

    # a = [0, 1, 2, ..., 16]
    a = range(17)

    # ii = C(17, 5)
    ii = combinations(a, 5)

    output_list_to_file(output_file, ii)
