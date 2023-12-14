#!/usr/bin/env python3
# coding: utf-8

'''
div 5 ... 3
div 8 ... 5
div 13 ... 11
'''

class Solution():
    ''' solution '''
    UPPER = 1000

    def __init__(self):
        self.ans = None

    @staticmethod
    def is_valid(n):
        ''' is valid '''
        return n % 5 == 3 and n % 8 == 5 and n % 13 == 11

    def action(self):
        ''' action '''
        print('action!')
        for n in range(self.UPPER, 1, -1):
            if self.is_valid(n):
                print(n,n%5,n%8,n%13)
                print()

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
