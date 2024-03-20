#!/usr/bin/env python3
# coding: utf-8
#

'''
Q16. 四位象棋選手參加一次迴圈賽，每兩人對戰一局，每局勝者得2分負者得0分,
和局則各得1分，已知全部比賽結束後，沒有人獲得全勝，而且每位選手得分均不同，
請問最多有多少局和局
'''

from itertools import combinations

class Solution():
    ''' to solve '''

    def __init__(self):
        self.vals = list(range(4))

    def action(self):
        ''' action '''
        print('action!')
        cnt = 0
        for t in combinations(self.vals, 2):
            cnt += 1
            print(t)
        print(f'checked {cnt} sets')

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
