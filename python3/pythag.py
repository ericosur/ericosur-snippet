#!/usr/bin/env python3
# coding: utf-8

'''
ref: https://zh.wikipedia.org/wiki/%E5%8B%BE%E8%82%A1%E6%95%B0

also refer to: triangle.py
'''

import re


class Solution():
    ''' solution '''

    # pythagon number pairs smaller than 100
    # lcm(p,q,r) = 1
    COPIED = '''
3   4   5
5   12  13
7   24  25
8   15  17
9   40  41
11  60  61
12  35  37
13  84  85
16  63  65
20  21  29
28  45  53
33  56  65
36  77  85
39  80  89
48  55  73
65  72  97
'''

    def __init__(self):
        self.pairs = []
        self.__parse_the_str()

    def __parse_the_str(self):
        ''' main '''
        a = Solution.COPIED.strip()
        for ln in a.splitlines():
            #print(ln)
            m = re.match(r'(\d+)\s+(\d+)\s+(\d+)', ln)
            if m:
                (p, q, r) = (m[1], m[2], m[3])
                self.pairs.append((p,q,r))

    def action(self):
        ''' print pairs as python code '''
        print('# python code style')
        print('pythag_pairs = [')
        for p in self.pairs:
            print(f'    {p},')
        print(']')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()


def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
