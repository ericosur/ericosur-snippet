#!/usr/bin/python3
# coding: utf-8

'''
given cli argument to get lower/upper prime

'''

import sys
import random
from lcp import LoadCompressPrime
from load_myutil import GetConfig

# pylint: disable=invalid-name
def test(argv, sp):
    ''' test '''
    print(sp)

    _max = sp.at(sp.get_count() - 1)
    _min = _max // 29
    if argv == []:
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 1
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
            if val > _max:
                print(f'[WARN] {val:,} is out of bound (max={_max:,})')
                continue
            ans = sp.list_nearby(val)
            if ans is None:
                print('[ERROR] error happens')
                continue

            isShown = False
            isPrime = False
            if len(ans) % 2 == 1:   # val is a prime
                isPrime = True

            for n in ans:
                if n == val:
                    print(f'prime idx#{sp.index(val)}  ', end='')
                if n > val and not isShown and not isPrime:
                    print('input ', val)
                    isShown = True
                print(n)
        except ValueError:
            print(f'    {ss} is a ValueError')
            continue

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("big")    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    cpfn = obj.get_full_path("compress_pickle")
    return txtfn, pfn, cpfn

def main(argv):
    ''' main function '''
    txtfn, _, cpfn = wrap_config()
    with LoadCompressPrime(txtfn, cpfn) as sp:
        test(argv, sp)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except IndexError:
        print('Must specify numbers to search nearby primes')
