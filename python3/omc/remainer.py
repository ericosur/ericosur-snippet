#!/usr/bin/env python3
#coding: utf-8

'''
https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E5%9B%BD%E5%89%A9%E4%BD%99%E5%AE%9A%E7%90%86

some number
divides by 5 remain 3
divides by 8 remain 5
divides by 13 remain 11
'''

# pylint: disable=invalid-name
class Solution():
    ''' class solution '''
    def __init__(self):
        self.r = [[5,3], [8,5], [13,11]]
        self.offset = 0
        self.M = 0

    def show_rules(self):
        ''' show rules '''
        (m1,m2,m3) = (self.r[0][0], self.r[1][0], self.r[2][0])
        (p1,p2,p3) = (self.r[0][1], self.r[1][1], self.r[2][1])
        print(f'div {m1} .. {p1}')
        print(f'div {m2} .. {p2}')
        print(f'div {m3} .. {p3}')

    def print_check(self):
        ''' print one result '''
        x = self.offset
        (m1,m2,m3) = (self.r[0][0], self.r[1][0], self.r[2][0])
        print(f'{x} % {m1} = {x%m1}')
        print(f'{x} % {m2} = {x%m2}')
        print(f'{x} % {m3} = {x%m3}')


    def action(self):
        ''' action '''
        (m1,m2,m3) = (self.r[0][0], self.r[1][0], self.r[2][0])
        (p1,p2,p3) = (self.r[0][1], self.r[1][1], self.r[2][1])
        M = m1 * m2 * m3
        M1 = m2 * m3
        M2 = m1 * m3
        M3 = m1 * m2
        r1 = M1 % m1
        r2 = M2 % m2
        r3 = M3 % m3
        offset = p1*M1*r1 + p2*M2*r2 + p3*M3*r3
        print(M1*r1%m1, M2*r2%m2, M3*r3%m3)
        self.offset = offset
        self.M = M
        print(f'{offset=}')
        print(f'x = {offset} + {M}k')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.show_rules()
        obj.action()
        obj.print_check()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
