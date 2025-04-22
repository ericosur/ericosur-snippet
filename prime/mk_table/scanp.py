#!/usr/bin/env python3
# coding: utf-8

'''
test some values in config file
'''

import sys

# pylint: disable=import-error
# pylint: disable=wrong-import-position
# ruff: noqa: E402
sys.path.insert(0, '../')
from store import GetConfig, StorePrime

MODNAME = "scanp"
VERSION = "2024.03.27"
CONFIG_KEY = "big"


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

def get_max_dist(primes) -> None:
    ''' max dist '''
    if not primes or len(primes) < 2:
        print("The primes list must contain at least two elements to calculate distances.")
        return

    ll = primes[0]
    uu = primes[-1]
    mm = 0
    pair = (0, 0)
    total = 0
    cnt = 0
    for i in range(1, len(primes)):
        lower_prime = primes[i-1]
        upper_prime = primes[i]
        d = abs(upper_prime - lower_prime)
        total += d
        cnt += 1
        if d > mm:
            mm = d
            pair = (lower_prime, upper_prime)
        # print(f'{lower_prime}--{d}--{upper_prime}')
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
