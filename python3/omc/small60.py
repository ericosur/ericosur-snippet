#!/usr/bin/python3
# coding: utf-8

'''
3 persons get 106 beads
how many way to take
'''

import itertools as it

class Solution():
    def __init__(self):
        self.m = [60, 7]
        self.n = [1000, -8]

    def find_answer(self):
        delta = 1000 - 60
        x = self.m[0]
        y = self.n[0]
        cnt = 0
        while True:
            x += self.m[1]
            y += self.n[1]
            cnt += 1
            d = y - x
            if d <= 0:
                break
            if d < delta:
                delta = d
        print(x, y, cnt, d)


def main():
    ''' main '''
    print('main')
    sol = Solution()
    sol.find_answer()

if __name__ == '__main__':
    main()
