#!/usr/bin/python3
# coding: utf-8

'''
given cli argument to get lower/upper prime

'''

import sys
import random
from load_myutil import GetConfig

MODNAME = 'nearby_primes.py'
OK_TO_USE_LCP = False
# small, big, large, h211...
CONFIG_KEY = 'small'

# pylint: disable=unused-import
try:
    import compress_pickle
    OK_TO_USE_LCP = True
except ImportError:
    pass

if OK_TO_USE_LCP:
    from lcp import LoadCompressPrime
else:
    from store_prime import StorePrime


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
    obj.set_configkey(CONFIG_KEY)    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    cpfn = obj.get_full_path("compress_pickle")
    return txtfn, pfn, cpfn

def main(argv):
    ''' main function '''
    txtfn, pfn, cpfn = wrap_config()
    if OK_TO_USE_LCP:
        with LoadCompressPrime(txtfn, cpfn) as sp:
            test(argv, sp)
    else:
        with StorePrime(txtfn, pfn) as sp:
            test(argv, sp)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except IndexError:
        print('Must specify numbers to search nearby primes')
