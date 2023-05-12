#!/usr/bin/env python3
# coding: utf-8

'''
some tips
https://github.com/gto76/python-cheatsheet
'''

import operator

# __pylint: disable=unused-variable
# __pylint: disable=unnecessary-pass
class Tip():
    ''' class tip '''
    def __init__(self):
        self._m = [1, 3, 5, 7, 9]
        self._n = [2, 4, 6, 8, 10]
        self._p = [11, 13, 17, 19, 23]
        self._q = None

    @staticmethod
    def title(s):
        ''' show title '''
        print(f'=====> {s} =====>')

    def tip1(self) -> None:
        ''' tip1 '''
        self.title('tip1')
        print('m:', self._m)
        print('n:', self._n)
        print('p:', self._p)
        print('sum of p:', sum(self._p))
        print('m + n:', self._m + self._n)

    def tip2(self) -> None:
        ''' tip2 '''
        self.title('tip2')
        # add m and n element by element
        s = [sum(p) for p in zip(self._m, self._n)]
        print('use zip:', s)
        # another way, need extra module
        s = list(map(operator.add, self._m, self._n))
        print('use operator, map')

    def tip3(self) -> None:
        ''' tip3 '''
        return self._q

    @classmethod
    def run(cls):
        ''' running tests '''
        obj = cls()
        obj.tip2()


def main():
    ''' main '''
    Tip.run()

if __name__ == '__main__':
    main()
