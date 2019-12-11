#!/usr/bin/env python3
# coding: utf-8

'''
In the game '17 pokers', combinations could be described as
C(17, 5). This script uses ''itertools.combinations'' to list
all possible combination.
'''
from itertools import combinations

PRINT_TO_STDOUT = False

def output_list_to_file(output_file, cclist):
    ''' output list to file '''
    with  open(output_file, "w") as text_file:
        cnt = 0
        for cc in cclist:
            if PRINT_TO_STDOUT:
                print(cc)
            text_file.write(str(cc)+'\n')
            cnt = cnt + 1
    print("output to file {}, total {} items".format(output_file, cnt))


def main():
    ''' main '''
    output_file = 'all-cmb.txt'

    # a = [0, 1, 2, ..., 16]
    a = range(17)

    # ii = C(17, 5)
    ii = combinations(a, 5)

    output_list_to_file(output_file, ii)

if __name__ == '__main__':
    main()
