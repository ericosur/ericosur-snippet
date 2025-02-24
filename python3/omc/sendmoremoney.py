#!/usr/bin/env python3
#coding: utf-8

'''
    S E N D
+   M O R E
------------
  M O N E Y
'''

from itertools import permutations


class Solution():
    ''' class solution '''
    def __init__(self):
        self.letters = {}
        self.tokens = list("SENDMORY")

    @staticmethod
    def is_valid(c):
        '''sendmory
           01234567
        '''

        c2 = []
        for i in c:
            c2.append(int(i))

        # here I can promise it is balanced
        # pylint: disable=unbalanced-tuple-unpacking
        assert len(c2) == 8
        # ruff: noqa: E741
        [S,E,N,D,M,O,R,Y] = c2
        if S==0 or M==0:
            return False
        #print(S,E,N,D,"+", M,O,R,E,end=' ')
        send = S*1000+E*100+N*10+D
        more = M*1000+O*100+R*10+E
        money = M*10000+O*1000+N*100+E*10+Y
        #print(send,more,money)
        if send + more == money:
            return True
        return False

    def action(self):
        ''' action '''
        msg='sendmoremoney'
        digits = list(msg)
        for d in digits:
            self.letters[d] = 1
        #print(self.letters)
        for c in permutations('9876543210',8):
            if self.is_valid(c):
                zipped = zip(self.tokens, c)
                for p in zipped:
                    print(p)
                break

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
