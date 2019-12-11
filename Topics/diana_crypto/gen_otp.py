#!/usr/bin/env python3
# coding: utf-8

'''
generate one-time pad in format of
5 char-word, 5 words a row, 4 rows
'''

import random

def gen_otp():
    ''' generate otp '''
    a2z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    opt_size = 5 * 5 * 4
    res = ""
    for i in range(opt_size):
        res = res + a2z[random.randint(0, len(a2z)-1)]
        if i % 25 == 24:
            res = res + '\n'
        elif i % 5 == 4:
            res = res + ' '
    return res

if __name__ == '__main__':
    REPEAT = 1
    for _ in range(REPEAT):
        print(gen_otp())
