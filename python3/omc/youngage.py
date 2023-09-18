#!/usr/bin/env python3
# coding: utf-8
#

'''
one guy who's age is the sum of birth year digits in 2017
'''

class Solution():
    ''' to solve '''
    UPPER = 2017

    def action(self):
        ''' action '''
        print('action!')
        for i in range(self.UPPER-1, 1900, -1):
            t = 2017 - i
            if t > 50:
                break
            digits = list(str(i))
            values = [int(x) for x in digits]
            if sum(values) == t:
                print(t, values)

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
