#!/usr/bin/env python3
# coding: utf-8

''' itertools '''

import itertools as it
import re
# https://stackoverflow.com/questions/17182656/how-do-i-iterate-through-the-alphabet
from string import ascii_uppercase

class Solution():
    ''' solution for checking missing combination '''
    def __init__(self):
        self.all_vals = set()
        self.csv_vals = set()
        self.radicals = dict()
        self.table = dict()

    def read_file(self, fn):
        ''' read file '''
        with open(fn, 'r') as f:
            for ll in f:
                m = re.search(r'[A-Z][A-Z]', ll)
                if m:
                    self.csv_vals.add(m.group(0))

    def make_all_combination(self):
        ''' make all combination for A-ZA-Z '''
        pp = list(ascii_uppercase)
        ccs = it.product(pp, pp)
        for ii in ccs:
            s = ii[0] + ii[1]
            self.all_vals.add(s)

    def read_table(self, fn):
        ''' read table '''
        with open(fn, 'r') as f:
            for ll in f:
                m = re.findall(r'^([a-z][a-z])\s+(\S+)$', ll)
                if m:
                    k = str(m[0][0]).upper()
                    v = m[0][1]
                    if k not in self.table:
                        self.table[k] = v

    def lookup_table(self, list_diff):
        ''' lookup orphan radicals in table '''
        print('list radicals not listed at table #1, #2, #3, #7 =====>')
        for _, ll in enumerate(list_diff):
            #print('[{}] {}: {}'.format(ii, ll, self.table[ll]))
            print('{},{}'.format(ll, self.table[ll]))

    def solve(self):
        ''' solve '''
        self.read_table('table.txt')    # whole boshiamy radicals
        self.read_file('gg.csv')        # 4 part of two-code table
        self.make_all_combination()
        print('len all({}) csv({})'.format(len(self.all_vals), len(self.csv_vals)))
        diff = self.all_vals.difference(self.csv_vals)
        list_diff = list(diff)
        list_diff.sort()
        self.lookup_table(list_diff)


def main():
    ''' main '''
    s = Solution()
    s.solve()

if __name__ == '__main__':
    main()
