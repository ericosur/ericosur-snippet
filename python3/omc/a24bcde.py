#!/usr/bin/env python3
# coding: utf-8
#

'''
ABCDE and EDCBA are both 24-multiple
find the smallest ABCDE
'''

class Solution():
    ''' search solution '''

    def __init__(self):
        pass

    def num2str(self, n):
        ''' num to str '''
        s = list(str(n))
        s2 = [s[4],s[3],s[2],s[1],s[0]]
        return (s, s2)

    def str2num(self, s):
        ''' str to num '''
        base = [10000, 1000, 100, 10, 1]
        v = 0
        for i in range(5):
            v = v + int(s[i]) * base[i]
        return v


    def isStrValid(self, s):
        ''' str is valid ? '''
        p = set(s)
        return len(p) == 5

    def isValid(self, n):
        ''' ABCDE and EDCBA '''
        if n < 10000 or n > 99999:
            return False
        if n%10==0:
            return False
        if n%24==0:
            return True
        return False

    def action(self):
        ''' action '''
        print('action!')
        cnt = 0
        for n in range(10000, 99999+1):
            if self.isValid(n):
                (s1, s2) = self.num2str(n)
                if self.isStrValid(s1) and self.isStrValid(s2):
                    r1 = self.str2num(s1)
                    r2 = self.str2num(s2)
                    if r1%24==0 and r2%24==0:
                        print(r1, r2)
                        break
                    cnt += 1
        print(f'{cnt=}')

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
