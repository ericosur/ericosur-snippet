#!/usr/bin/python3
# coding: utf-8

'''
given cli argument to get lower/upper prime

'''

import argparse
import random
from store import GetConfig

MODNAME = 'nearby_primes.py'
VERSION = '2024.03.11'
USE_LCP = False


if USE_LCP:
    from store import LoadCompressPrime
else:
    from store import StorePrime

def sep():
    ''' sep '''
    print('--------------------------')


class NearbyPrimes():
    ''' list nearby primes '''

    # small, big, large, h211...
    CONFIG_KEY = 'big'
    _min = 101

    def __init__(self):
        ''' init '''
        self.values = []
        self._verbose = False
        self._debug = False
        self.prime = None
        self._max = -1


    def validate_values(self):
        ''' validate values '''
        self._max = self.prime.at(self.prime.get_count() - 1)
        if self.values == []:
            if self.verbose:
                print(f"Use random number between {self._min}, {self._max}")
                sep()
            REPEAT = 1
            for _ in range(REPEAT):
                r = random.randint(self._min, self._max)
                self.values.append(r)
            return

        tmps = self.values
        ok_values = []
        for v in tmps:
            if v < 10:    # too small...
                continue
            if v > self._max:
                print(f'[WARN] {v:,} is out of bound (max={self._max:,})')
                continue
            ok_values.append(v)
        self.values = ok_values

    def show_answers(self, ans, val):
        ''' show answers '''
        if self.debug:
            print(f'{val=}')
            print(f'len: {len(ans)}, {ans}')
            return

        is_prime = False
        is_show = False
        if len(ans) % 2 == 1:   # val is a prime
            is_prime = True
        for n in ans:
            if n == val:
                print(f'prime idx#{self.prime.index(val)}  ', end='')
            if n > val and not is_show and not is_prime:
                print('input: ', val)
                is_show = True
            print(n)

    def query_primes(self):
        ''' list primes '''
        self.validate_values()
        for v in self.values:
            try:
                ans = self.prime.list_nearby(v)
                if ans is None:
                    print('[ERROR] error happens')
                    continue
                self.show_answers(ans, v)
                if v != self.values[-1]:
                    sep()
            except ValueError:
                print(f'ValueError while {v}')
                continue

    @staticmethod
    def wrap_config():
        ''' wrap config and retrieve settings '''
        conf = GetConfig()
        conf.set_configkey(NearbyPrimes.CONFIG_KEY)    # change this to use larger table
        txtfn = conf.get_full_path("txt")
        pfn = conf.get_full_path("pickle")
        cpfn = conf.get_full_path("compress_pickle")
        return txtfn, pfn, cpfn


    def show_prime_obj(self):
        ''' show prime obj '''
        if self.verbose:
            print(self.prime)
            sep()


    def action(self):
        ''' main function '''
        txtfn, pfn, cpfn = NearbyPrimes.wrap_config()

        if self.debug:
            #print(f'{self.verbose=}')
            print(f'{self.values=}')
            print(f'{txtfn=}\n{pfn=}\n{cpfn=}')

        if USE_LCP:
            self.prime = LoadCompressPrime(txtfn, cpfn,
                verbose=self.verbose, debug=self.debug)
        else:
            self.prime = StorePrime(txtfn, pfn,
                verbose=self.verbose, debug=self.debug)

        self.prime.get_ready()
        self.show_prime_obj()
        self.query_primes()


    def set_values(self, values):
        ''' set values '''
        self.values = values

    @property
    def debug(self) -> bool:
        ''' title of notification '''
        return self._debug
    @debug.setter
    def debug(self, val: bool):
        ''' setter of title '''
        self._debug = val

    @property
    def verbose(self) -> bool:
        ''' title of notification '''
        return self._verbose
    @verbose.setter
    def verbose(self, val: bool):
        ''' setter of title '''
        self._verbose = val

    @classmethod
    def run(cls, values, verbose, debug):
        ''' run me '''
        obj = cls()
        obj.verbose = verbose
        obj.debug = debug
        obj.set_values(values)
        obj.action()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='list nearby primes from specified number')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("values", metavar='vals', type=int, nargs='*',
        help="some values")
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    parser.add_argument("-d", "--debug", action='store_true', default=False,
        help='debug mode')
    args = parser.parse_args()

    NearbyPrimes.run(args.values, args.verbose, args.debug)


if __name__ == '__main__':
    main()
