#!/usr/bin/python3
# coding: utf-8

'''
[goldbach's conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)

given an even number and list some sum of two primes

* import from store_prime using table prime_100k (100 killo primes)
* import from sip, it uses larger table
'''

import bisect
import sys
from random import randint
import time
from load_myutil import get_largedata_path

MODNAME = "goldbach"
LCP_LOADED = False

try:
    # larger and slower
    from lcp import LoadCompressPrime as StorePrime
    print(f'[INFO] {MODNAME}: use **LoadCompressPrime**')
    LCP_LOADED = True
except ImportError:
    # smaller and quicker
    from store_prime import StorePrime
    print(f'[INFO] {MODNAME}: use **store_prime**')

# pylint: disable=invalid-name
# too-many-statements

def index(a, x):
    '''
    get index of the leftmost value exactly equal to value **x** from list **a**
    return -1 if not found
    '''
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def impl1(val, ret):
    ''' impl1 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        if left in ret:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time

def impl2(val, ret):
    ''' impl2 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        try:
            ret.index(left)
        except ValueError:
            pass
        else:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time

def impl3(val, ret):
    ''' impl3 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        try:
            index(ret, left)
        except ValueError:
            pass
        else:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time

class Goldbach():
    ''' find goldbach '''
    MAX_REPEAT = 3
    MAX_SHOW = 7
    MIN_ANS_LEN = 10

    def __init__(self, values=None):
        self.curr = 0
        self.values = None

        if values is None or values == []:
            self.values = []
            self._gen_values()
        else:
            self.values = values

        txtfn, pfn, pzfn = get_largedata_path()
        if LCP_LOADED:
            self.sp = StorePrime(txtfn, pzfn)
        else:
            self.sp = StorePrime(txtfn, pfn)
        self.sp.__enter__()
        print(self.sp)

    def __exit__(self, exc_type, exc_value, traceback):
        ''' exit '''
        del self.sp

    def _gen_values(self):
        ''' gen values '''
        _min = 21
        _max = 197
        for _ in range(self.MAX_REPEAT):
            self.values.append(randint(_min, _max) * 2)

    def run_goldbach(self):
        ''' it could be found if val < 4 * 10^17 '''
        for v in self.values:
            if v % 2 != 0:
                print(f'[ERROR] {v} must be an even number')
                continue

            ret = self.sp.get_primes_less_than(v)
            if ret is None:
                print(f'{MODNAME}: no primes less than {v}')
                continue

            self.curr = v
            # ans, cnt, duration = impl1(v, ret)
            # ans, cnt, duration = impl2(v, ret)
            ans, _, duration = impl3(v, ret)

            self.output_answer(ans, duration)

    def output_answer(self, ans, duration):
        ''' output answers '''
        if ans is None:
            print(f'{MODNAME}: no answers for {self.curr}')
            return

        print(f'\nFor {self.curr}, goldbach pairs: {len(ans)}, time: {duration:.2e} seconds')
        if len(ans) <= self.MIN_ANS_LEN:
            for i in ans:
                print(i)
        else:
            self.pick_from_list(ans, self.MAX_SHOW)

    def pick_from_list(self, ans, cnt):
        ''' pick cnt items from ans '''
        if len(ans) <= self.MIN_ANS_LEN:
            print('[WARN] the size of answers MUST > 10, len=',len(ans))
        #print(f'{ans[0]}, {ans[len(ans)//2]}, {ans[-1]}')
        randoms = [0, len(ans)//2, len(ans)-1]
        # generate enough and unique numbers
        pick_num = 0
        while pick_num < cnt:
            r = randint(1, len(ans)-2)
            if r in randoms:
                continue
            randoms.append(r)
            pick_num += 1
        randoms.sort()
        msg = ''
        s = slice(0, len(randoms)-1)
        for r in randoms[s]:
            msg = msg + f'{ans[r]}, '
        msg = msg + f'{ans[-1]}'
        print(msg)

    @staticmethod
    def print_duration(start, end, msg=''):
        ''' print duration '''
        print(f'{MODNAME}: {msg} duration: {end-start:.3e} seconds (wall clock)')

    def action(self):
        ''' action '''
        self.run_goldbach()

    @classmethod
    def run(cls, values):
        ''' run me '''
        obj = cls(values)
        obj.action()

def main(argv):
    ''' main '''
    values = []
    # type change from str to int from command line arguments
    if len(argv) > 0:
        for i in argv:
            try:
                v = int(i)
                if v%2 == 1:
                    print(f'[WARN] given {i} is ODD number, skip')
                    continue
                values.append(v)
            except ValueError:
                print(f'[WARN] given {i} is invalid, skip')

    Goldbach.run(values)

if __name__ == '__main__':
    main(sys.argv[1:])
