#!/usr/bin/env python3
# coding: utf-8

'''
test StorePrime
'''

import argparse
import random
import sys
from load_myutil import GetConfig
from store_prime import StorePrime

LCP_READY = False
try:
    from lcp import LoadCompressPrime
    LCP_READY = True
except ImportError:
    print('[WARN] no such module: LoadCompressPrime')

def test(argv, sp):
    ''' test '''
    print(sp)
    _max = sp.at(sp.get_count() - 1)
    _min = sp.at(0)

    if argv == []:
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 3
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
            if val < _min or val > _max:
                print(f'[ERROR] {val} is out of bound!')
                continue
            (p, q) = sp.get_around(val)
            show_result(sp, val, p, q)
        except ValueError:
            print(f'    {ss} is a ValueError')
            continue

def make_arrow(lower, v, upper):
    '''
    for example, this function returns ===#=== or --#----
    example lines like the following lines

    914863 is in the range of (914861 =#=== 914867)
    831004 is in the range of (830989 ----#------ 831023)

    equal sign means this is actual numbers between two primes
    minus sign mean it is ratio between two primes
    '''
    s = ''
    max_len = 11
    step = '-'
    if upper - lower < max_len:
        max_len = upper - lower - 1
        step = '='

    r = int(abs(v-lower)/(upper-lower) * max_len)
    for i in range(max_len):
        if i == r:
            s += "#"
        else:
            s += step
    return s

def test_arrow():
    print(make_arrow(12,13,14))
    print(make_arrow(11,15,19))

def show_result(sp, v, p, q):
    ''' show result, not using StorePrime.show() '''
    NAME = 'show_result'
    if p is None and q is None:
        print(f'{NAME} no results')
        return
    if q is None:
        print(f'{v} is a {p+1}th prime')
        return
    upper = sp.at(q)
    lower = sp.at(p)
    arrow = make_arrow(lower, v, upper)
    print(f'{v} is in the range of ({lower} {arrow} {upper})')

def main():
    ''' main function '''
    parser = argparse.ArgumentParser(description='''
        example scripts to run module sp or lcp
        to test if specified integers are prime numbers or not
    ''', usage='''
    (auto)     $ run_example.py
    (integers) $ run_example.py 97 101 307''')
    parser.add_argument("ints", metavar='int', type=int, nargs='*',
        help="specify some integers to test primes")
    #parser.add_argument("-v", "--verbose", action='store_true', help='verbose')
    parser.add_argument("-l", "--lcp", action='store_true', help='run lcp, LoadCompressPrime')
    parser.add_argument("-1", "--small", action='store_true', help='use small config')
    parser.add_argument("-2", "--big", action='store_true', help='use big config')
    parser.add_argument("-3", "--large", action='store_true', help='use large config')
    parser.add_argument("-4", "--h119", action='store_true', help='use h119 config')
    args = parser.parse_args()

    obj = GetConfig()
    if args.small:
        obj.set_configkey("small")
    elif args.big:
        obj.set_configkey("big")
    elif args.large:
        obj.set_configkey("large")
    elif args.h119:
        obj.set_configkey("h119")
    else:
        obj.set_configkey("small")

    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    cpfn = obj.get_full_path("compress_pickle")

    if args.lcp and LCP_READY:
        print('args.lcp...')
        with LoadCompressPrime(txtfn=txtfn, pfn=cpfn) as lcp:
            test(args.ints, lcp)
    else:
        print('args.sp...')
        with StorePrime(txtfn=txtfn, pfn=pfn) as sp:
            test(args.ints, sp)

if __name__ == '__main__':
    main()
