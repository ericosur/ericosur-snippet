#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
from pylab import plot, show, gcf, gca
from math import log

'''
想知道階乘和次方增加速度
例如 25 的 n 次方 vs n 的階乘

畫圖之後會發現階乘會比次方增加的速度還快
BASE 越大交叉的點會在越後面

X 軸是 n, Y 軸是取 ln() 的值
'''


BASE = 25


def get_factorial(n):
    '''
    if get_factorial(n) is already calculated, it would not
    re-calculate it again.
    '''
    global stepvalues

    if n <= 2:
        return 1
    elif n in stepvalues:
        # print '.',
        return stepvalues[n]
    else:
        # print 'c',
        stepvalues[n] = n * get_factorial(n - 1)
        return stepvalues[n]


def load_pickle():
    '''
    載入 pickle，若無則建立預設的值
    '''
    global stepvalues
    try:
        inf = open(data_file, "r")
        stepvalues = cPickle.load(inf)
        inf.close()
    except IOError:
        stepvalues = {1:1, 2:2}    # init values


def save_pickle():
    '''
    儲存 stepvalues 至 pickle
    '''
    global stepvalues
    # store into pickle file
    ouf = open(data_file, "w")
    cPickle.dump(stepvalues, ouf)
    ouf.close()


stepvalues = {}
data_file = 'stepvalues.p'

if __name__ == '__main__':
    load_pickle()

    fact = []   # base !
    expo = []   # base ** n

    for i in xrange(1,100):
        fact.append( log(get_factorial(i)) )
        expo.append( log(BASE ** i) )

#    t = xrange(1,20)
    plot(fact, color='red')     # 階乘
    plot(expo, color='green')   # 次方

    setfig = gca()
    setfig.set_label("base 20 ")
    setfig.set_xlabel("factorial(red) vs exponient(green)")
    setfig.set_ylabel("ln( f(x) )")
    show()

    save_pickle()

'''
    # if you want to save plot to image file
    fig = gcf()
    fig.savefig("test.png")
'''
