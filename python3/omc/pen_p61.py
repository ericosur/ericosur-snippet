#!/usr/bin/python3
# coding: utf-8

'''
'''

class Solution():
    TOTAL = 100
    def __init__(self):
        self.p = 0
        self.e = 0
        self.n = 0

    @staticmethod
    def check(n, p, e):
        return 3*e > n > 2*p > 8*e/3

    def action(self):
        '''  action '''
        # n > p > e
        cnt = 0
        for n in range(100,1,-1):
            for p in range(100-n, 1,-1):
                for e in range(100-n-p, 1,-1):
                    if n > p > e:
                        if n+p+e == 100:
                            cnt += 1
                            if self.check(n,p,e):
                                print(f'{n=}, {p=}, {e=}')
        #print(f'{cnt=}')

    @classmethod
    def run(cls):
        obj = cls()
        obj.action()


def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
