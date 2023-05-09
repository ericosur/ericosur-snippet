#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
天干地支

甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥

'''

from datetime import datetime
#import time

class GanChi():
    ''' 提供 天干地支紀年有關的功能 '''
    MAGIC_START = 2997
    PREV_CYCLES = 3
    YEAR_PER_CYCLE = 60
    NUM_GNN = 10
    NUM_YAL = 12
    PREDATA = ["甲乙丙丁戊己庚辛壬癸","子丑寅卯辰巳午未申酉戌亥",
        "鼠牛虎兔龍蛇馬羊猴雞狗豬"]

    def __init__(self):
        self.gnn = list(self.PREDATA[0])
        self.yal = list(self.PREDATA[1])
        self.sesue = list(self.PREDATA[2])

    def __str__(self):
        return '\n'.join(self.PREDATA)

    def get_gnn(self):
        ''' 傳回 天干 '''
        return self.gnn

    def get_yal(self):
        ''' 傳回 地支 '''
        return self.yal

    def get_ses(self):
        ''' 傳回 生肖 '''
        return self.sesue

    @classmethod
    def get_class(cls):
        ''' get class '''
        #print(cls.__name__)
        return cls()

    def normalize_year(self, y):
        ''' y > -2997 and y != 0'''
        if y == 0:
            raise ValueError("ERROR: cannot assign 0 as year")
        if y < 0:
            _y = y + self.MAGIC_START
            if _y < 0:
                raise ValueError("ERROR: too old to use GanChi")
        else:
            _y = y + self.MAGIC_START - 1
        return _y

    def to_gc(self, y):
        ''' to_gc '''
        _y = self.normalize_year(y)
        g = self.gnn[_y % self.NUM_GNN]
        y = self.yal[_y % self.NUM_YAL]
        s = self.sesue[_y % self.NUM_YAL]
        res = f'{g}{y}({s})'
        return res

    def get_reminder(self, y):
        ''' reminder '''
        _y = self.normalize_year(y)
        _y = y + self.MAGIC_START - 1
        g = _y % self.NUM_GNN
        y = _y % self.NUM_YAL
        return (g, y)

    @staticmethod
    def check_ab(m=0, n=0):
        ''' check a and b '''
        return (0 <= m < 10) and (0 <= n < 12) and ((m+n)%2==0)

    def brute_force_try(self, gnn, yal):
        ''' given 天干 (from 0) 地支 (from 0)  guess year '''
        this_year = datetime.today().year
        test_year = 0
        found = False
        # after this year
        answers = []
        for i in range(self.YEAR_PER_CYCLE):
            test_year = this_year + i
            (_m, _n) = self.get_reminder(test_year)
            if _m == gnn and _n == yal:
                print(test_year, self.to_gc(test_year))
                found = True
                break

        if not found:
            return []

        _y = test_year
        answers.append(test_year)
        for i in range(self.PREV_CYCLES):
            _y -= 60
            print(_y)
            answers.append(_y)

        return answers

    def test0(self):
        ''' test '''
        for y in [-2997, -720, 1894, 1912, 1975, 1995, 2012, 2023]:
            res = self.to_gc(y)
            print(f'{y} is {res}')

    def test1(self):
        ''' test 1 '''
        self.brute_force_try(-1, -1)
        self.brute_force_try(0, 0)
        self.brute_force_try(6, 0)
        self.brute_force_try(0, 6)
        self.brute_force_try(9, 9)
        self.brute_force_try(10, 10)
        self.brute_force_try(11, 11)
        self.brute_force_try(9, 11)

    def run(self):
        ''' run test '''
        self.test0()
        self.test1()

def do_values(values, radius=0):
    '''main function'''
    gc = GanChi()
    center = 0
    try:
        center = int(radius)
    except ValueError:
        print('[WARN] center must be an integer:', radius)
        center = 0
    for y in values:
        #print(f'y: {y}')
        for r in range(y-center, y+center+1):
            #print(f'r: {r}')
            res = gc.to_gc(r)
            print(f'{r} is {res}')
    del gc

def do_tests():
    ''' test '''
    test = GanChi.get_class()
    test.run()

def do_verbose():
    ''' verbose '''
    gc = GanChi()
    print(gc)
    del gc

def do_ab(m, n):
    ''' do ab '''
    gc = GanChi.get_class()
    g = gc.get_gnn()
    y = gc.get_yal()
    ret = ""
    if gc.check_ab(m, n):
        ret = f'{g[m]} {y[n]}'
    else:
        print(f'ERROR: invalid input: {m}, {n}')
        return

    ans = gc.brute_force_try(m, n)
    if not ans:
        print(f'ERROR: invalid year: {ret}')


def main():
    ''' main '''
    print("[INFO] please run ganzhi.py, will run tests here")
    do_tests()

if __name__ == '__main__':
    main()
