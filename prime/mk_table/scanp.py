#!/usr/bin/env python3
# coding: utf-8

'''
test some values in config file
'''

import sys

MODNAME = "scanp"
VERSION = "2023.10.30"
CONFIG_KEY = "big"

# pylint: disable=import-error
# pylint: disable=wrong-import-position

sys.path.insert(0, '../')
from load_myutil import GetConfig
from store_prime import StorePrime


def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey(CONFIG_KEY)    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    #cpfn = obj.get_full_path("compress_pickle")
    return txtfn, pfn

def do_test():
    ''' perform tests '''
    txtfn, pfn = wrap_config()
    sp = StorePrime(txtfn=txtfn, pfn=pfn)
    sp.get_ready()
    #ll = sp.at(0)
    uu = sp.get_maxprime()
    primes = sp.get_primes_less_than(uu)
    get_max_dist(primes)

def get_max_dist(primes):
    ''' max dist '''
    ll = primes[0]
    uu = primes[-1]
    mm = -1
    total, cnt = 0, 0
    pair = ()
    for i in range(1, len(primes)):
        l = primes[i-1]
        u = primes[i]
        d = abs(u-l)
        total += d
        cnt += 1
        if d > mm:
            mm = d
            pair = (l, u)
        #print(f'{l}--{d}--{u}')
    print(f'max dist between primes {ll} to {uu} = {mm} while {pair}')
    print(f'avg dist = {total/cnt:.3f}')


def trivia_test():
    ''' main '''
    primes = [
        2,3,5,7,11,
        13,17,19,23,29,
        31,37,41,43,47,
        53,59,61,67,71,
        73,79,83,89,97
    ]
    assert len(primes) == 25
    get_max_dist(primes)

def main():
    ''' main '''
    do_test()

if __name__ == '__main__':
    main()
