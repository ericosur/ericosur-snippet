#!/usr/bin/env python3
# coding: utf-8
#

'''
5 pirates, 10 locks, only 3 guys could unlock all locks
each guy takes 6 keys
'''

class Solution():
    ''' to solve '''
    def __init__(self):
        self.locks = [0 for _ in range(10)]


    def action(self):
        ''' action '''
        print('action!')
        print(self.locks)

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
