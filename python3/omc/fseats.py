#!/usr/bin/env python3
# coding: utf-8

'''
╳〇
'''

import itertools as it


# pylint: disable=too-many-instance-attributes
class Solution():
    ''' find seats '''
    def __init__(self):
        self.seats = []
        self.qi = self.zz = self.tnb = self.ti = self.aqp = -1
        self.msg = ''
        self.miss = self.got = 0
        self.clear()

    def clear(self):
        ''' clear '''
        self.qi = -1
        self.zz = -1
        self.tnb = -1
        self.ti = -1
        self.aqp = -1
        self.msg = ''
        self.miss = 0
        self.got = 0

    def print_seat(self):
        ''' print seats '''
        s = self.seats
        p = ['甲','乙', '丙', '丁', '戊']
        print(p[s[0]], p[s[1]], p[s[2]], p[s[3]], p[s[4]], s)

    def basic_data(self):
        ''' where '''
        self.qi = self.seats.index(0)
        self.zz = self.seats.index(1)
        self.tnb = self.seats.index(2)
        self.ti = self.seats.index(3)
        self.aqp = self.seats.index(4)

    def append_symbol(self, yes_no):
        ''' add symbol '''
        if yes_no:
            self.got += 1
            return '〇'
        self.miss += 1
        return '✗'

    def collect_ret(self, whoami):
        ''' collect ret '''
        print(f'{whoami}: {self.msg}, {self.got} vs {self.miss}')
        ret = self.got == 2 and self.miss == 1
        self.clear()
        return ret

    def check_zz(self):
        '''
        乙: 有兩個人在我和丙之間。甲離丙最遠。我和戊相鄰
        乙=1
        '''
        self.clear()
        self.basic_data()
        d = abs(self.zz - self.tnb)
        self.msg.join(self.append_symbol(d == 3))
        d = abs(self.qi - self.tnb)
        self.msg.join(self.append_symbol(d == 4))
        d = abs(self.zz - self.aqp)
        self.msg.join(self.append_symbol(d == 1))

        r = self.collect_ret(' check_zz')
        return r

    def check_tnb(self):
        '''
        丙: 我和戊相鄰。我也和乙相鄰。有兩個人在我和甲之間
        丙=2
        '''
        self.clear()
        self.basic_data()
        d = abs(self.tnb - self.aqp)
        self.msg.join(self.append_symbol(d == 1))
        d = abs(self.tnb - self.zz)
        self.msg.join(self.append_symbol(d == 1))
        d = abs(self.tnb - self.qi)
        self.msg.join(self.append_symbol(d == 3))

        r = self.collect_ret('check_tnb')
        return r

    def check_aqp(self):
        '''
        戊: 我離丙最遠。我和乙相鄰。有一個人在我和丁之間。
        戊=4
        '''
        self.clear()
        self.basic_data()
        d = abs(self.aqp - self.tnb)
        self.msg.join(self.append_symbol(d == 4))
        d = abs(self.aqp - self.zz)
        self.msg.join(self.append_symbol(d == 1))
        d = abs(self.aqp - self.ti)
        self.msg.join(self.append_symbol(d == 2))

        r = self.collect_ret('check_aqp')
        return r

    def action(self):
        ''' action '''
        symbols = [0, 1, 2, 3]
        cnt = 0
        #got_ans = False
        for n in it.permutations(symbols, 4):
            n = list(n)
            n.insert(2, 4)
            self.seats = n
            if n[0] == 4:
                continue
            self.print_seat()
            match = 0
            if self.check_aqp():
                match += 1
            if self.check_zz():
                match += 1
            if self.check_tnb():
                match += 1
            if match == 3:
                print("this one matched!")
                #got_ans = True
                self.print_seat()
                break
            cnt += 1
            if cnt > 999999999:
                break
        print(f'{cnt=}')

    @classmethod
    def run(cls):
        ''' runme '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
