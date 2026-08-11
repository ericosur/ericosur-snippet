#!/usr/bin/env python3
# coding: utf-8

'''
Q7: 已知二位數 ab 且 ab / (a+b) = q .. r
r的最大值？
'''

class Solution():
    ''' class to find solution '''
    LOWER=10
    UPPER=99

    def __init__(self):
        pass

    def check_val(self, n):
        ''' check val '''
        a = n // 10
        b = n % 10
        if a+b == 0:
            print(f"ERROR: {n}: div by zero")
            return -1
        q = n // (a+b)
        r = n % (a+b)
        if a+b > 14:
            print(f'{n} / ({a}+{b}) = {q} .. {r}')
        return r

    def action(self):
        ''' check all '''
        ceil = 0
        for n in range(self.LOWER, self.UPPER+1):
            r = self.check_val(n)
            if r > ceil:
                ceil = r
                print(n, r)


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
