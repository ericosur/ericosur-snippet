#!/usr/bin/env python3
# coding: utf-8

'''
P25 Q14 有一些四位數ABCD，各位數上的數字互不相同，
使得AB，BC，CD 都是質數，那麼所有這樣的四位數有多少個？
'''


class Solution():
    ''' try to find solution '''

    primes = {
            13, 17, 19, 23, 29,
            31, 37, 41, 43, 47,
            53, 59, 61, 67, 71,
            73, 79, 83, 89, 97}

    def __init__(self):
        self.n = 0
        self.digits = []

    def validate(self, n):
        ''' validate '''
        self.digits = list(str(n))

        # only the first digit could be even
        ds = { int(x) for x in self.digits[1:] }
        ev = {0,2,4,6,8}

        if len(ds.intersection(ev)):
            self.digits = []
            self.n = 0
            return False

        s = set(self.digits)
        # four digits are different
        if len(s)==4:
            self.n = n
            return True

        self.digits = []
        self.n = 0
        return False

    def cut3(self):
        ''' abcd cut to ab, bc, cd '''
        vs = [ int(x) for x in self.digits ]
        ab = vs[0]*10+vs[1]
        bc = vs[1]*10+vs[2]
        cd = vs[2]*10+vs[3]
        abcd = ((vs[0]*10+vs[1])*10+vs[2])*10+vs[3]
        assert self.n==abcd
        if ab in self.primes and bc in self.primes and cd in self.primes:
            #print(f'{self.n=} {ab=} {bc=} {cd=} {abcd=}')
            return abcd
        return None

    def action(self):
        ''' action '''
        matched = 0
        (lv0, lv1, lv2, lv3) = (0,0,0,0)
        ans = {}
        for i in range(1000, 9999+1):
            lv0 += 1
            if self.validate(i):
                lv1 += 1
                r = self.cut3()
                if r is not None:
                    matched += 1
                    k = r // 1000
                    if k not in ans:
                        ans[k] = []
                    ans[k].append(r)
                else:
                    lv2 += 1
            else:
                lv3 += 1
        print(f'{lv0=} {lv1=} {lv2=} {lv3=} {matched=}')
        for _,v in ans.items():
            print(v)

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
