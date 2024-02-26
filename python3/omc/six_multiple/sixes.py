#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=too-many-instance-attributes

'''
from 19 to 99 take 2 different number, product is 6's multiple
'''

from itertools import combinations

class Solution():
    ''' to solve '''

    def __init__(self):
        self.vals = list(range(19, 100))
        self.cnt23 = 0
        self.cnt32 = 0
        self.cnt61 = 0
        self.cnt62 = 0
        self.v61s = []
        self.v62s = []
        self.v23s = []
        self.v32s = []

    def is2(self, n):
        ''' 2 and only 2's multiple '''
        return n%2==0

    def is3(self, n):
        ''' 3 and only 3's multiple '''
        return n%3==0

    def is6(self, n):
        ''' 6's multiple '''
        return n%6==0

    def action(self):
        ''' action '''
        print('action!')
        cnt = 0
        pass_cnt = 0
        dd={}
        for t in combinations(self.vals, 2):
            #print(t)
            cnt += 1
            assert t[0]!=t[1]

            sixOr6 = 0
            sixAnd6 = 0
            if self.is6(t[0]) or self.is6(t[1]):
                sixOr6 += 1
            if self.is6(t[0]) and self.is6(t[1]):
                sixAnd6 += 1

            if self.is6(t[0]):
                self.cnt61 += 1
                self.v61s.append(t)
            elif self.is6(t[1]):
                self.cnt62 += 1
                self.v62s.append(t)

            elif self.is2(t[0]) and self.is3(t[1]):
                self.cnt23 += 1
                self.v23s.append(t)

            elif self.is3(t[0]) and self.is2(t[1]):
                self.cnt32 += 1
                self.v32s.append(t)
                if t[0] not in dd:
                    dd[t[0]] = []
                dd[t[0]].append(t[1])

            if (t[0]*t[1])%6 == 0:
                #print(t)
                pass_cnt += 1

        print(f'or6:{sixOr6}, and6:{sixAnd6}')
        print(f'got {cnt} sets, {pass_cnt=}')
        print(f'{self.cnt61=}, {self.cnt62=}')
        print(f'{self.cnt23=}, {self.cnt32=}')
        self.output2file('cnt61.txt', self.v61s)
        self.output2file('cnt62.txt', self.v62s)
        self.output2file('cnt23.txt', self.v23s)
        self.output2file('cnt32.txt', self.v32s)

        print(f'{len(dd.keys())=}')
        for k,v in dd.items():
            print(k,len(v), v)



    def output2file(self, fn, vals):
        ''' output to files '''
        with open(fn, "wt", encoding='UTF-8') as fobj:
            for n in vals:
                print(n, file=fobj)

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
