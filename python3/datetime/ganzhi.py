#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
天干地支

甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥

'''

from __future__ import print_function
from datetime import datetime
import time

class GanChi():
    MAGIC_START = 2997

    def __init__(self):
        self.gnn = list("甲乙丙丁戊己庚辛壬癸")
        self.sesue = list("鼠牛虎兔龍蛇馬羊猴雞狗豬")
        self.yal = list("子丑寅卯辰巳午未申酉戌亥")

    def to_gc(self, y):
        ''' to_gc '''
        if y == 0:
            raise ValueError("ERROR: cannot assign 0 as year")
        if y < 0:
            _y = y + self.MAGIC_START
        else:
            _y = y + self.MAGIC_START - 1
        g = self.gnn[_y % 10]
        y = self.yal[_y % 12]
        s = self.sesue[_y % 12]
        res = f'{g}{y}({s})'
        return res

    def get_reminder(self, y):
        ''' reminder '''
        _y = y + self.MAGIC_START - 1
        g = _y % 10
        y = _y % 12
        return (g, y)

    def brute_force_try(self, gnn, yal):
        ''' given 天干 (from 0) 地支 (from 0)  guess year '''
        this_year = datetime.today().year
        max_try = 60
        test_year = 0
        # after this year
        for i in range(max_try):
            test_year = this_year + i
            (_m, _n) = self.get_reminder(test_year)
            if _m == gnn and _n == yal:
                print(test_year, self.to_gc(test_year))
                break
        _y = test_year
        for i in range(4):
            _y -= 60
            print(_y)

    def test0(self):
        ''' test '''
        for y in [-720, 1894, 1912, 1975, 1995, 2012, 2023]:
            res = self.to_gc(y)
            print(f'{y} is {res}')

    def test1(self):
        ''' test 1 '''
        self.brute_force_try(0, 0)
        self.brute_force_try(6, 0)
        self.brute_force_try(0, 6)

    def run(self):
        self.test0()
        self.test1()

def main():
    '''main function'''
    gc = GanChi()
    gc.run()


if __name__ == '__main__':
    main()
