#!/usr/bin/python3
# coding: utf-8

'''
P43 Q15 用160個花片排成空心正十邊形或排成空心正八邊形，
兩種圖形的邊長花片數之和是多少個？
'''

import sys


class Solution():
    ''' try to find solution '''

    def action(self):
        ''' action '''
        for i in range(10,20):
            print(i, i * 10 - 10)
        print('----------')
        for j in range(14,22):
            print(j, j*8 - 8)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()


def main():
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
