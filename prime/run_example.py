#!/usr/bin/env python3
# coding: utf-8

'''
test StorePrime
'''

import argparse
import random
from load_myutil import get_largedata_path, get_bigdata_path
from store_prime import StorePrime
from lcp import LoadCompressPrime


def test(argv, sp):
    ''' test '''
    print(sp)
    #rint(sp.get_count())

    if argv == []:
        _max = sp.at(sp.get_count() - 1)
        _min = sp.at(0)
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 10
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
            sp.test(val)
        except ValueError:
            print(f'    {ss} is a ValueError')
            continue


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
    args = parser.parse_args()

    txtfn, pfn, _ = get_bigdata_path()
    print(f'{__file__}: {txtfn=}, {pfn=}')

    if args.lcp:
        print('args.lcp...')
        with LoadCompressPrime() as lcp:
            test(args.ints, lcp)
    else:
        print('args.sp...')
        with StorePrime(txtfn, pfn) as sp:
            test(args.ints, sp)

if __name__ == '__main__':
    main()
