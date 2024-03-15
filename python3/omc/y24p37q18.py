#!/usr/bin/env python3
# coding: utf-8
#

'''
P37 Q18 {19,20,21,...,78,79} 這組數中選取兩個不同的數，
使得它們的和為偶數的選法有多少種？
'''

from itertools import combinations

class Solution():
    ''' to solve '''

    def __init__(self):
        self.vals = list(range(19, 80))

    def action(self):
        ''' action '''
        print('action!')
        cnt = 0
        even_cnt = 0
        for t in combinations(self.vals, 2):
            #print(t)
            cnt += 1
            assert t[0]!=t[1]
            if (t[0]+t[1])%2 == 0:
                even_cnt += 1
        print(f'checked {cnt} sets, {even_cnt=}')

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
