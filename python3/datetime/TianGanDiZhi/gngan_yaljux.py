#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
This module provides utility functions and class GanChi
天干地支

甲子  乙丑  丙寅  丁卯  戊辰  己巳  庚午  辛未  壬申  癸酉  甲戌  乙亥
丙子  丁丑  戊寅  己卯  庚辰  辛巳  壬午  癸未  甲申  乙酉  丙戌  丁亥
戊子  己丑  庚寅  辛卯  壬辰  癸巳  甲午  乙未  丙申  丁酉  戊戌  己亥
庚子  辛丑  壬寅  癸卯  甲辰  乙巳  丙午  丁未  戊申  己酉  庚戌  辛亥
壬子  癸丑  甲寅  乙卯  丙辰  丁巳  戊午  己未  庚申  辛酉  壬戌  癸亥

'''

import sys
from typing import Tuple, List
from datetime import datetime

console = None
USE_RICH = False
try:
    from rich.console import Console
    console = Console()
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    #print("[WARN] no rich.console to use")
    pass

def do_nothing(*args, **wargs) -> None:
    ''' do nothing '''
    return None

def get_thisyear() -> int:
    ''' get this year '''
    return datetime.today().year

class GanChi():
    ''' 提供 天干地支紀年有關的功能 '''
    MAGIC_START = 2997
    PREV_CYCLES = 3
    YEAR_PER_CYCLE = 60
    NUM_GNN = 10
    NUM_YAL = 12
    PREDATA = ["甲乙丙丁戊己庚辛壬癸","子丑寅卯辰巳午未申酉戌亥",
        "鼠牛虎兔龍蛇馬羊猴雞狗豬"]

    def __init__(self, log=do_nothing):
        self.log = log
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
    def run(cls, log):
        ''' run test '''
        #print(cls.__name__)
        obj = cls(log)
        #obj.test0()
        obj.test1()

    def normalize_year(self, y: int) -> int:
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

    def to_gc(self, y: int) -> str:
        ''' to_gc '''
        _y = self.normalize_year(y)
        g = self.gnn[_y % self.NUM_GNN]
        y = self.yal[_y % self.NUM_YAL]
        s = self.sesue[_y % self.NUM_YAL]
        res = f'{g}{y}({s})'
        return res

    def get_reminder(self, y: int) -> Tuple[int, int]:
        ''' reminder '''
        _y = self.normalize_year(y)
        _y = y + self.MAGIC_START - 1
        g = _y % self.NUM_GNN
        y = _y % self.NUM_YAL
        return (g, y)

    @staticmethod
    def check_ab(m:int=0, n:int=0, log=do_nothing) -> bool:
        ''' check a and b '''
        logd = log
        if m<0 or m>9:
            logd(f'check_ab: out of range: {m=}')
            return False
        if n<0 or n>11:
            logd(f'check_ab: out of range: {n=}')
            return False
        if (m+n)%2 != 0:
            logd(f'check_ab: not pass the rule {m}+{n} is even')
            return False
        #return (0 <= m < 10) and (0 <= n < 12) and ((m+n)%2==0)
        return True

    def brute_force_try(self, gnn: int, yal: int, log=do_nothing) -> list:
        ''' given 天干 (from 0) 地支 (from 0)  guess year '''
        logd = log
        #logd(f"brute_force_try: {gnn=}, {yal=}")
        # check the parameters, will not proceed if invalid
        if not self.check_ab(gnn, yal):
            return []
        this_year = get_thisyear()
        test_year = 0
        found = False
        # after this year
        answers = []
        for i in range(self.YEAR_PER_CYCLE):
            test_year = this_year + i
            (_m, _n) = self.get_reminder(test_year)
            if _m == gnn and _n == yal:
                #print(test_year, self.to_gc(test_year))
                found = True
                break

        if not found:
            return []

        _y = test_year
        answers.append(test_year)
        for i in range(self.PREV_CYCLES):
            _y -= 60
            logd(f"brute_force_try: found: {_y}")
            answers.append(_y)
        answers.sort()
        return answers

    def test0(self) -> None:
        ''' test #0 '''
        logd = self.log
        logd("test0...")
        console.print('[INFO] I [red]DO NOT recommend[/red] year in negative value')
        for y in [-2997, -720, 1894, 1912, 1975, 1995, 2012, 2023]:
            res = self.to_gc(y)
            print(f'{y} is {res}')

    def test1(self) -> None:
        ''' test #1 '''
        logd = self.log
        def run_test(m: int, n: int, expect: List[int]) -> None:
            ''' check the ans '''
            logd(f'run_test: {m},{n}')
            ans = self.brute_force_try(m, n, log=do_nothing)
            if expect is None:
                logd(f'ans: {ans}')
                return
            if expect == ans:
                console.print('pass')
            else:
                console.print('FAIL')

        logd("test1...")
        run_test(-3, 0, [])
        run_test(0, -3, [])
        run_test(-1, -1, [])
        run_test(-1, 0, [])
        run_test(0, -1, [])
        run_test(0, 0, [1864,1924,1984,2044])
        run_test(1, 4, [])
        run_test(1, 3, [1855,1915,1975,2035])
        run_test(6, 0, [1900,1960,2020,2080])
        run_test(7, 1, [1901,1961,2021,2081])
        run_test(9, 0, [])
        run_test(9, 1, [1853,1913,1973,2033])
        run_test(10, 2, [])
        run_test(2, 12, [])

def show(color: str, msg: str) -> None:
    ''' show '''
    if not USE_RICH:
        print(msg)
        return
    rprint(f'[{color}]{msg}')

def do_values(values: List[int], target=0, radius: int=0, log=do_nothing) -> None:
    '''main function'''
    logd = log
    gc = GanChi(logd)
    center = 0
    try:
        center = int(radius)
    except ValueError:
        logd('[WARN] center must be an integer:', radius)
        center = 0
    logd(f'do_values: {values=}')
    logd(f'{center=}')
    this_year = get_thisyear()
    for y in values:
        for r in range(y-center, y+center+1):
            res = gc.to_gc(r)
            msg = f'{r} is {res}'
            if r==this_year:
                if r==target:
                    show('red', msg) # both
                else:
                    show('green', msg) # this year
            elif r==target:
                show('yellow', msg)  # target year
            else:
                show('white', msg)  # normal
    del gc

def do_verbose(log=do_nothing) -> None:
    ''' verbose '''
    logd = log
    logd("do_verbose...")
    gc = GanChi()
    print(gc)
    del gc

def do_ab(m: int, n: int, log=do_nothing) -> None:
    ''' do ab, m is {0,9}, n is {0, 11}
        and pass rule of check_ab()
    '''
    logd = log
    gc = GanChi(logd)
    g = gc.get_gnn()
    y = gc.get_yal()
    ret = ""
    if gc.check_ab(m, n, logd):
        ret = f'{g[m]}{y[n]}'
    else:
        logd(f'ERROR: invalid input: {m}, {n}')
        return
    ans = gc.brute_force_try(m, n, log=log)
    if not ans:
        logd(f'ERROR: no answer for {ret}')
    logd(f'do_ab: {ans=}')
    this_year = get_thisyear()
    for i in ans:
        msg = f"{i} {gc.to_gc(i)}"
        if i==this_year:
            show('yellow', msg)
        else:
            show('white', msg)

def do_tests(log=do_nothing) -> None:
    ''' run the original tests'''
    GanChi.run(log)

if __name__ == "__main__":
    print(f'This script {sys.argv[0]} provides functions.')
    print("DO NOT run this directly")
    print("try: cli_tester.py, ganzhi.py, or typer_gng.py")
