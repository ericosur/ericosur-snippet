#!/usr/bin/env python3
# coding: utf-8
#

'''
P40 Q30. {1,2,3,...,49,50} 這 50 個數中，
取出若干個數使得其中任意兩個數的和都不能被 7 整除，
那麼最多可以取出多少個數？
'''

from itertools import combinations

SUPER_LAZY = True

class Solution():
    ''' to solve '''
    def __init__(self):
        self.vals = list(range(1, 50+1))

    def has_seven(self, the_pair):
        '''
        return true, if any breaks the rule
        return false, never found

        '''
        for q in combinations(the_pair, 2):
            (m, n) = q
            if (m+n)%7 == 0:
                return True
        return False

    def check_turn(self, n):
        ''' pick n
        return True means there is at least one combination that matches
        the condition, and will not check further
        '''
        cnt = 0
        for p in combinations(self.vals, n):
            cnt += 1
            if self.has_seven(p):
                print(f'{n}: {p} breaks')
                return True

        print(f'{n}: out of {cnt}')
        return False

    def action(self):
        ''' action '''
        print('action!')
        for n in range(50,3,-1):
            ret = self.check_turn(n)
            if ret:
                print(f'for {n} has seven multiples, go next...')
                continue
            print(f'for {n}, never seven multiples combinations...')


    def save_q(self, n, q):
        ''' save q '''
        fn = f'qualified{n:02d}.txt'
        with open(fn, 'wt', encoding='utf-8') as fobj:
            for i in q:
                print(i, file=fobj)
        print(f'output to {fn}')

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
