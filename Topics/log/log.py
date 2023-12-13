#!/usr/bin/env python
# coding: utf-8

''' math.log '''

import math


def demo_log():
    ''' demo '''
    vals = [1, 2.7182818284, 10, 100, 300]
    for vv in vals:
        print(f'{vv:.5f}: {math.log(vv):.5f} -- {math.log10(vv):.5f}')

if __name__ == '__main__':
    demo_log()
