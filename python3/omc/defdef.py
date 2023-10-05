#!/usr/bin/env python3
#coding: utf-8

'''
      D E F
+     D E F
------------
  A B C D A
'''

from itertools import permutations

class Solution():
    ''' class solution '''
    def __init__(self):
        self.letters = {}

    @staticmethod
    def is_valid(c):
        '''
           012345
        '''
        c2 = []
        for i in c:
            c2.append(int(i))

        # pylint: disable=unbalanced-tuple-unpacking
        assert len(c2)==6
        [A,B,C,D,E,F]=c2
        if D==0 or A==0:
            return False
        p = 100*D+10*E+F
        q = 10000*A+1000*B+100*C+10*D+A
        if p*p == q:
            return True
        return False

    def action(self):
        ''' action '''
        for c in permutations('0123456789',6):
            if self.is_valid(c):
                print(c)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
