#!/usr/bin/env python3
# coding: utf-8

'''
test StorePrime
'''

import argparse
import random
import sys
from the_prt import prt

MODNAME = 'run_example'

try:
    from store import StorePrime, GetConfig, make_arrow, dbg
except ImportError as err:
    prt('[FAIL] cannot load necessary module:', err)
    sys.exit(1)

try:
    from store import LoadCompressPrime
    LCP_READY = True
except ImportError:
    LCP_READY = False
    dbg('[WARN] cannot load module: LoadCompressPrime')

def test(argv, sp):
    ''' test '''
    REPEAT = 10
    prt(sp)
    _max = sp.at(sp.get_count() - 1)
    _min = sp.at(0)

    if argv == []:
        #prt(f"max:{_max}, min:{_min}")
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
            if val < _min or val > _max:
                prt(f'[ERROR] {val:,} is out of bound!')
                continue
            (p, q) = sp.get_around(val)
            show_result(sp, val, p, q)
        except ValueError:
            prt(f'    {ss} is a ValueError')
            continue

def show_result(sp, v, p, q):
    ''' show result, not using StorePrime.show() '''
    NAME = 'show_result'
    if p is None and q is None:
        prt(f'{NAME} no results')
        return
    if q is None:
        prt(f'{v} is a {p+1}th prime')
        return
    upper, lower = sp.at(q), sp.at(p)
    arrow = make_arrow(lower, v, upper)
    prt(f'{v}:({lower} {arrow} {upper})')

def wrap_config(args):
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    if args.small:
        obj.set_configkey("small")
    elif args.big:
        obj.set_configkey("big")
    elif args.large:
        obj.set_configkey("large")
    elif args.h119:
        obj.set_configkey("h119")
    elif args.h422:
        obj.set_configkey("h422")
    else:
        obj.set_configkey("small")

    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    cpfn = obj.get_full_path("compress_pickle")
    return txtfn, pfn, cpfn

def logd(*args, **wargs):
    ''' local logd '''
    prt(f'{MODNAME}:', *args, **wargs)

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
    parser.add_argument("-5", "--h422", action='store_true', help='use h119 config')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    parser.add_argument("-d", "--debug", action='store_true', default=False,
        help='debug mode')

    args = parser.parse_args()

    txtfn, pfn, cpfn = wrap_config(args)
    if args.debug:
        prt(f'run_example: {txtfn=}, {pfn=}, {cpfn=}')

    if args.lcp:
        if not LCP_READY:
            prt('[ERROR] Cannot use _*_LoadCompressPrime_*_')
            sys.exit(1)
        logd('Using LoadCompressPrime...')
        with LoadCompressPrime(txtfn=txtfn, pfn=cpfn, debug=args.debug,
            verbose=args.verbose) as lcp:
            test(args.ints, lcp)
    else:
        logd('Using StorePrime...')
        with StorePrime(txtfn=txtfn, pfn=pfn, debug=args.debug,
            verbose=args.verbose) as sp:
            test(args.ints, sp)

if __name__ == '__main__':
    main()
