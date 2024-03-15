#!/usr/bin/env python3
# coding: utf-8
#

'''
P32 Q30. 從集合 {19,20,21,..., 97,98,99}
選取兩個不同的數，使得它們的乘積能被6整除的選法有多少種？
'''

from itertools import combinations

def swap(m, n):
    ''' swap '''
    return n, m

class Solution():
    ''' to solve '''

    def __init__(self):
        self.vals = list(range(19, 100))

    def action(self):
        ''' action '''
        print('action!')
        cnt = 0
        match_cnt = 0
        for t in combinations(self.vals, 2):
            cnt += 1
            (m, n) = t
            if (m*n)%6 == 0:
                match_cnt += 1
                print(t)
        print(f'checked {cnt} sets')
        print(f'match {match_cnt} sets')


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
