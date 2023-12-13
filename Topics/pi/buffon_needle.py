#!/usr/bin/env python3
# coding: utf-8

'''
reference: http://blog.linux.org.tw/~jserv/archives/002004.html
reference: http://www.mste.uiuc.edu/reese/buffon/
'''

import math
from random import random


def throw_needle():
    ''' throw needle '''
    max_try = 99991
    crossing = 0

    for _ in range(max_try):
        theta = math.pi * random()  # 0 <= theta < pi
        x = random()    # 0 <= x < 1
        if x <= 0.5 * math.sin(theta):  # crossing
            crossing += 1

    est_pi = float(max_try) / float(crossing)
    err = abs(est_pi - math.pi) / math.pi * 100
    print(f'try {max_try} and crossing {crossing}, '
        f'est pi = {est_pi:.6f}, err = {err:.4f}')
    return (err, est_pi)    # return a tuple for err and pi

def main():
    ''' main '''
    repeat = 100
    result = {}
    for _ in range(repeat):
        t = throw_needle()
        result[t[0]] = t[1] # store returned tuple to dict

    print(f"after {repeat} repeats, the nearest pi = "
        f"{result[min(result)]:.6f}, err = {min(result):.4f}%")
    print(f"after {repeat} repeats, the nearest pi = "
        f"{result[max(result)]:.6f}, err = {max(result):.4f}%")

if __name__ == '__main__':
    main()
