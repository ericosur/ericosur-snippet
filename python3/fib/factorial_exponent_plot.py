#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
想知道階乘和次方增加速度
例如 25 的 n 次方 vs n 的階乘

畫圖之後會發現階乘會比次方增加的速度還快
BASE 越大交叉的點會在越後面

X 軸是 n, Y 軸是取 ln() 的值
'''

from math import log

from calc_factorial import CalcFactorial
from pylab import gca, gcf, plot, show

# if you want to save plot to image file, turn it True
OPTION_SAVEIMAGE = False

def main():
    ''' main '''
    BASE = 25
    MAXREPEAT = 100

    nlvl = []   # base !
    expo = []   # base ** n

    with CalcFactorial() as fact:
        for i in range(1, MAXREPEAT):
            nlvl.append(log(fact.factorial(i)))
            expo.append(log(BASE ** i))

#    t = xrange(1,20)
    plot(nlvl, color='red')     # 階乘
    plot(expo, color='green')   # 次方

    setfig = gca()
    setfig.set_label("base 20 ")
    setfig.set_xlabel("factorial(red) vs exponient(green)")
    setfig.set_ylabel("ln( f(x) )")
    show()

    if OPTION_SAVEIMAGE:
        fig = gcf()
        fig.savefig("test.png")


if __name__ == '__main__':
    main()
