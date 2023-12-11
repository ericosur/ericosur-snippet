#!/usr/bin/env python
# coding: utf-8

''' math.log '''

import math


def demo_log():
    ''' demo '''
    vals = [1, 2.7182818284, 10, 100, 300]
    for vv in vals:
        print("%.5f: %.5f -- %.5f" % (vv, math.log(vv), math.log10(vv)))


if __name__ == '__main__':
    demo_log()
