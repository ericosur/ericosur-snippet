#!/usr/bin/env python3
# coding: utf-8
#

'''
abcd x 4 = dcba
a = 2
'''

class Solution():

    def init(self):
        pass

    # @staticmethod
    # def is_valid(n):


    def action(self):
        ''' action '''
        print('action!')
        for p in range(2000, 2999):
            q = p * 4
            if q > 9999:
                continue
            qs = list(str(q))
            ps = list(str(p))
            if ps[0] == qs[3] and ps[1] == qs[2] and ps[2] == qs[1] and ps[3] == qs[0]:
                print(p, q)




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
