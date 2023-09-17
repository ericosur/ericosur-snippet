#!/usr/bin/env python3
#coding: utf-8

'''
https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E5%9B%BD%E5%89%A9%E4%BD%99%E5%AE%9A%E7%90%86

make one number and make the rule

'''

import random

class Solution():
    ''' class solution '''
    def __init__(self):
        self.r = [[3,1], [5,1], [7,5]]
        self.primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        self.n = 0

    def show_rules(self):
        ''' show rules '''
        (m1,m2,m3) = (self.r[0][0], self.r[1][0], self.r[2][0])
        (p1,p2,p3) = (self.r[0][1], self.r[1][1], self.r[2][1])
        print(f'div {m1} .. {p1}')
        print(f'div {m2} .. {p2}')
        print(f'div {m3} .. {p3}')
        print(f'self.r = [[{m1},{p1}], [{m2},{p2}], [{m3},{p3}]]')

    def print_check(self, x):
        ''' print one result '''
        (m1,m2,m3) = (self.r[0][0], self.r[1][0], self.r[2][0])
        r1 = x % m1
        r2 = x % m2
        r3 = x % m3
        print(f'{x} % {m1} = {r1}')
        print(f'{x} % {m2} = {r2}')
        print(f'{x} % {m3} = {r3}')
        (self.r[0][1], self.r[1][1], self.r[2][1]) = (r1,r2,r3)

    def action(self):
        ''' action '''
        ps = self.primes
        m1 = random.choice(ps)
        ps.remove(m1)
        m2 = random.choice(ps)
        ps.remove(m2)
        m3 = random.choice(ps)
        ps.remove(m3)

        tmp = [m1,m2,m3]
        (m1,m2,m3) = sorted(tmp)
        #print(m1,m2,m3)
        (self.r[0][0], self.r[1][0], self.r[2][0]) = (m1,m2,m3)

        n = random.randint(m3, m3+m1)
        #print(f'{n=}')

        self.print_check(n)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()
        obj.show_rules()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
