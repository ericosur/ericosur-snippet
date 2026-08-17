#!/usr/bin/env python3

'''
($10,$20,$50) (4,4,4)
to pay $230, how many methods?
'''



class Solution:
    ''' class solution '''

    def __init__(self):
        self.limit = 230
        self.c = [50,20,10]

    def action(self):
        ''' action '''
        for p in range(5):
            for q in range(5):
                for r in range(5):
                    t = p*50+q*20+r*10
                    #print(t,p,q,r)
                    if t == self.limit:
                        print(p,q,r,"=>", t)

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
