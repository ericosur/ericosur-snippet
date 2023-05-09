#!/usr/bin/env python3
# coding: utf-8

'''
transfer between account, not want to see four
'''

import random

# pylint: disable=too-many-arguments

class Solution():
    ''' try to find solution '''
    def __init__(self, lower, upper, src=None, dst=None, rand=True, debug=False):
        self.debug = debug
        self.random = rand
        if src:
            self.fubon = src
        else:
            self.fubon = [18107, 50000]
        if dst:
            self.ctbc = dst
        else:
            self.ctbc = [20601, 5176, 50000]
        self.check_accounts()
        if upper <= lower:
            raise ValueError("upper must be larger than lower")
        self.upper = upper
        self.lower = lower
        self.last_try = -1
        self.report_init()

    def check_accounts(self):
        ''' check values in accounts is valid '''
        for m in self.fubon:
            if m < 0:
                raise ValueError("src account must >= 0")
        for n in self.ctbc:
            if n < 0:
                raise ValueError("dst account must >= 0")

    @staticmethod
    def has_digit4(val):
        ''' check if has digit 4 '''
        s = str(val)
        l = list(s)
        #print(s)
        for c in l:
            if c == '4':
                return True
        return False

    def report_init(self):
        ''' report init variables '''
        print(f'lower:{self.lower}, upper:{self.upper}')
        print(f'fubon: {self.fubon}')
        print(f'ctbc: {self.ctbc}')
        print("----------")

    def pick_value(self):
        ''' pick value between lower to upper '''
        if self.random:
            #print('USE random method...')
            return self.pick_value_random()
        #print('USE increasing number method...')
        return self.pick_value_inc()


    def pick_value_random(self):
        ''' pick value from random '''
        t = random.randint(self.lower, self.upper)
        self.last_try = t
        if self.debug:
            print('use random: {t}')
        return t

    def pick_value_inc(self):
        ''' pick value increasingly '''
        if self.last_try <= 0:
            t = self.lower
        else:
            t = self.last_try + 1
        self.last_try = t
        if self.debug:
            print(f'2nd: t is {t}')
        return t


    def run(self):
        ''' find a proper ammount to meet all criteria '''
        need_more_try = True
        repeat = 0
        while need_more_try:
            t = self.pick_value()
            repeat += 1
            if self.has_digit4(t):
                ''' try again '''
                if self.debug:
                    print(f'{t} is not good')
                continue
            if self.test_fubon(t) and self.test_ctbc(t):
                need_more_try = False
                self.report(t)
            if repeat > (self.upper - self.lower):
                msg = f"NO ANSWER: repeat too many times: {repeat}"
                raise ValueError(msg)
        print(f"[INFO] has tried {repeat} times")

    def report(self, t):
        ''' report the result '''
        print(f'take out from src: {t}')
        self.fubon[0] -= t
        sumup = sum(self.fubon)
        print(f'src: {self.fubon}, total: {sumup}')
        self.ctbc[0] += t
        sumup = sum(self.ctbc)
        print(f'dst: {self.ctbc}, total: {sumup}')

    def test_fubon(self, take_out):
        ''' minus amount out of fubon '''
        tmp = self.fubon.copy()
        f0 = tmp[0] - take_out
        if f0 < 0:
            if self.debug:
                print(f"take too much out: {take_out}")
            return False
        if self.has_digit4(f0):
            if self.debug:
                print(f'single term has four: {tmp} takes {take_out}')
            return False
        tmp[0] = f0
        sumup = sum(tmp)
        if self.has_digit4(sumup):
            if self.debug:
                print(f'total sum has four: {sumup} takes {take_out}')
            return False
        # all pass
        return True

    def test_ctbc(self, pour_in):
        ''' minus amount out of fubon '''
        tmp = self.ctbc.copy()
        f0 = tmp[0] + pour_in
        if self.has_digit4(f0):
            if self.debug:
                print(f'single term has four: {f0} takes {pour_in}')
            return False
        tmp[0] = f0
        sumup = sum(tmp)
        #print(f'sumup: {sumup}')
        if self.has_digit4(sumup):
            if self.debug:
                print(f'total sum has four: {sumup} takes {pour_in}')
            return False
        # all pass
        return True

    def test(self):
        ''' test '''
        assert self.has_digit4("0000000000") is False
        assert self.has_digit4("") is False
        assert self.has_digit4("1234") is True
        assert self.has_digit4("49876532") is True

        assert self.test_fubon(3) is False
        assert self.test_fubon(4000) is False
        assert self.test_fubon(20000) is False

        assert self.test_ctbc(3) is False
        assert self.test_ctbc(307) is False
        print("pass")

def main():
    ''' main '''
    src = [15891, 17733, 39000]
    dst = [1693, 50000]
    sol = Solution(200, 500, src=src, dst=dst, rand=False, debug=False)
    sol.run()

if __name__ == '__main__':
    main()

# yuanta, 2876, -4068
