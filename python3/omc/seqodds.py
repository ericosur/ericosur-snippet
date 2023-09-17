#!/usr/bin/env python3
# coding: utf-8
#

'''
sum of serial odds = 60
sum of serial evens = 60
'''


class Solution():
    LIMIT = 60
    def init(self):
        self.odds = []
        self.evens = []

    @staticmethod
    def gen_odd(k):
        if k < 0:
            raise ValueError
        return 2*k+1

    @staticmethod
    def gen_even(k):
        if k < 0:
            raise ValueError
        return 2*k

    @staticmethod
    def get_values(k, n, isOdd=True):
        ''' n is length '''
        nums = []
        tmp = k
        for i in range(n):
            if isOdd:
                v = Solution.gen_odd(tmp)
            else:
                v = Solution.gen_even(tmp)
            tmp += 1
            nums.append(v)
        return nums

    def action(self):
        ''' action '''
        print('action!')
        for i in range(2, 10):
            for k in range(60):
                v = Solution.get_values(k, i, True)
                if sum(v) == 60:
                    print(f'Odds: len:{i}, {k=}, {v}')
                v = Solution.get_values(k, i, False)
                if sum(v) == 60:
                    print(f'Evens: len:{i}, {k=}, {v}')

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
