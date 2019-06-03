#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' list perfect square number into csv '''

from __future__ import print_function
import os
import csv

def gen_csv(fn):
    ''' generate csv '''
    with open(fn, 'wt', encoding='UTF-8') as csvfile:
        fieldnames = ['index', 'n', 'value']
        sw = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        sw.writeheader()
        lower = 31
        upper = 99
        cnt = 0
        for n in range(lower, upper):
            cnt = cnt + 1
            sw.writerow({'index': cnt, 'n':n, 'value':n*n})


def main():
    ''' main '''
    OUTPUT_CSV = 'perfect_s.csv'
    if os.path.isfile(OUTPUT_CSV):
        print("remove existed file...")
        os.remove(OUTPUT_CSV)

    print("generating {}...".format(OUTPUT_CSV))
    gen_csv(OUTPUT_CSV)


if __name__ == '__main__':
    main()
