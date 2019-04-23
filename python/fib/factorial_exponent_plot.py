#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
想知道階乘和次方增加速度
例如 25 的 n 次方 vs n 的階乘

畫圖之後會發現階乘會比次方增加的速度還快
BASE 越大交叉的點會在越後面

X 軸是 n, Y 軸是取 ln() 的值
'''

from pylab import plot, show, gcf, gca
from math import log

# for class CalcFactorial
from calc_factorial import CalcFactorial


def main():
    BASE = 25
    MAXREPEAT = 100

    fact = []   # base !
    expo = []   # base ** n

    with CalcFactorial() as foo:
        for i in range(1, MAXREPEAT):
            fact.append( log(foo.factorial(i)) )
            expo.append( log(BASE ** i) )

#    t = xrange(1,20)
    plot(fact, color='red')     # 階乘
    plot(expo, color='green')   # 次方

    setfig = gca()
    setfig.set_label("base 20 ")
    setfig.set_xlabel("factorial(red) vs exponient(green)")
    setfig.set_ylabel("ln( f(x) )")
    show()


'''
    # if you want to save plot to image file
    fig = gcf()
    fig.savefig("test.png")
'''

if __name__ == '__main__':
    main()
