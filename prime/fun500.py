#!/usr/bin/python3
# coding: utf-8

'''
testing LoadCompressPrime/store_prime
'''

from random import randint
from store import GetConfig

CONFIG_KEY = 'small'

USE_LCP_MODULE = None
try:
    from store import LoadCompressPrime as StorePrime
    USE_LCP_MODULE = True
except ImportError:
    from store import StorePrime
    USE_LCP_MODULE = False

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey(CONFIG_KEY)    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    pfn = obj.get_full_path("pickle")
    cpfn = obj.get_full_path("compress_pickle")
    return txtfn, pfn, cpfn

class Goldbach():
    ''' easy version of goldbach '''
    max_len = 7

    def __init__(self):
        txtfn, pfn, cpfn = wrap_config()
        if USE_LCP_MODULE:
            self.sp = StorePrime(txtfn=txtfn, pfn=cpfn)
        else:
            self.sp = StorePrime(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()
        self.val = -1
        self.picks = None

    @staticmethod
    def pick_from_list(ans, cnt):
        ''' pick cnt items from ans '''
        if len(ans) <= cnt:
            return ans

        #print(f'will pick {cnt} items')
        randoms = [0, len(ans)//2, len(ans)-1]
        # generate enough and unique numbers
        pick_num = len(randoms)
        while pick_num < cnt:
            r = randint(1, len(ans)-2)
            if r in randoms:
                continue
            randoms.append(r)
            pick_num += 1
        randoms.sort()

        rets = []
        for r in randoms:
            rets.append(ans[r])
        return rets


    def set_val(self, val):
        ''' set val '''
        if val % 2 == 0:
            self.val = val
            print(f'input value: {val}')
        else:
            self.val = -1
            raise ValueError("MUST positive even number")


    def output_picks(self):
        ''' output picks '''
        for i,p in enumerate(self.picks):
            print(f'({p}, {self.val - p}), ', end='')
            if i and i%5==4:
                print()
        print()


    def gold_bach(self, val):
        ''' goldbach '''
        self.set_val(val)

        primes = self.sp.get_primes_less_than(val)
        self.picks = None
        if isinstance(primes, list):
            print(f'total length of primes less than {val}: {len(primes)}')
            if len(primes) <= self.max_len:
                self.picks = primes
            else:
                self.picks = self.pick_from_list(primes, self.max_len)
        self.output_picks()

    def action(self):
        ''' demo action '''
        val = 500
        #val = randint(50, 500) * 2  # must be even number
        self.gold_bach(val)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Goldbach.run()

if __name__ == '__main__':
    main()
