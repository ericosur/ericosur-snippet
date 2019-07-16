#!/usr/bin/env python3
# coding: utf-8

'''
some tips
https://github.com/gto76/python-cheatsheet
'''

# pylint: disable=unused-variable
# pylint: disable=invalid-name
# pylint: disable=unnecessary-pass
class Tip():
    ''' class tip '''
    def __init__(self):
        self.m = [1, 3, 5, 7, 9]
        self.n = [2, 4, 6, 8, 10]
        self.p = [11, 13, 17, 19, 23]

    @staticmethod
    def title(s):
        ''' show title '''
        print('=====> {} =====>'.format(s))

    def tip1(self):
        ''' tip1 '''
        self.title('tip1')
        print('m:', self.m)
        print('n:', self.n)
        print('p:', self.p)
        print('sum of p:', sum(self.p))
        print('m + n:', self.m + self.n)

    def tip2(self):
        ''' tip2 '''
        self.title('tip2')
        # add m and n element by element
        s = [sum(p) for p in zip(self.m, self.n)]
        print('use zip:', s)
        # another way, need extra module
        import operator
        s = list(map(operator.add, self.m, self.n))
        print('use operator, map')

    def tip3(self):
        ''' tip3 '''
        pass

    def test(self):
        ''' running tests '''
        self.tip3()

def main():
    ''' main '''
    tip = Tip()
    tip.test()

if __name__ == '__main__':
    main()
