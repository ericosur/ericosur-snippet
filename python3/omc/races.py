#!/usr/bin/env python3
# coding: utf-8
#

'''
若干支球隊參加一次足球循環賽，每兩支球隊之間賽一場，
每場比賽，勝者積3分，敗者1分，如果打平兩隊各得2分，
全部比賽結束後，全部球隊的積分之和是24分。
請問有多少支球隊參加了這次比賽？
'''

from itertools import combinations

class Solution():
    ''' to solve '''
    def __init__(self):
        self.points = {}

    def total_race(self, n):
        ''' 場比賽 '''
        if n < 2:
            raise ValueError
        return n*(n-1)//2

    def make_list(self, n):
        ''' make a list like (a,b,c) from given number '''
        if n < 1 or n > 25:
            raise ValueError
        chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return chars[0:n]


    def calculate_score(self, pair):
        ''' give team, A, B got three possible scores '''

        (p, q) = pair
        if p not in self.points:
            self.points[p] = 0
        if q not in self.points:
            self.points[q] = 0

        self.points[p] += 1
        self.points[q] += 1

    def show_results(self):
        ''' show results '''
        print(self.points)

    def clear_results(self):
        ''' clear '''
        for k in self.points.keys():
            self.points[k] = 0

    def simulate_race(self, n):
        ''' simulate '''
        for i in range(n):
            print('3,1')
            print('2,2')
            print('1,3')

    def action(self):
        ''' action '''
        print('action!')
        for n in range(2, 5):
            r = self.total_race(n)
            print(f'{n=}: {r=}')
            # self.simulate_race(r)
            # print('---')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main() -> None:
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
