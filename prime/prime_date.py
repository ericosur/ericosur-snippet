#!/usr/bin/python3
# coding: utf-8

'''
https://blog.oldj.net/2019/05/24/%E7%B4%A0%E6%95%B0%E6%97%A5/?fbclid=IwAR25olIU4Hg92N-BxVx12N5Id7JpJrHpQBgSis4BssIwwZF9LPFRZysoTVU

for example: 20190823
20190823 is prime
 0190823 is prime
  190823 is prime
   90823 is prime
    0823 is prime
     823 is prime
      23 is prime
       3 is prime
yay! it's a prime day

Note that your prime number table should cover the test number or you cannot
find any prime dates.
'''

from datetime import date, timedelta
from time import time
import sys
from load_myutil import GetConfig
try:
    from lcp import LoadCompressPrime
    print('[INFO] use **LoadCompressPrime**')
except ImportError:
    print("[FAIL] cannot import LoadCompressPrime")
    sys.exit(1)

MODNAME = "prime_date.py"

# pylint: disable=invalid-name
# too-many-statements

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3f} sec')

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("large")    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    cpfn = obj.get_full_path("compress_pickle")
    return txtfn, cpfn

class TestDate():
    ''' test date is a prime '''
    def __init__(self):
        txtfn, cpfn = wrap_config()
        self.sp = LoadCompressPrime(txtfn=txtfn, pfn=cpfn)
        self.sp.get_ready()

    def test(self, argv: str):
        ''' test_prime_date '''
        v = argv
        allprime = True

        for _ in range(len(v)):
            if self.sp.index(int(v)) == -1:
                #print('{} not a prime'.format(v))
                allprime = False
                break
            # else:
            #     print('{:>8s} is PRIME'.format(v))
            v = v[1:]
        if allprime:
            print(f'{argv} is a prime day!')
        return allprime

    def run(self):
        ''' run '''
        start_d = date(2000, 1, 1)
        end_d = date(2099, 12, 31)
        curr = start_d
        cnt = 0
        start = time()
        while curr <= end_d:
            ds = curr.strftime('%Y%m%d')    # YYYYmmdd, ie: 20190823
            if self.test(ds):
                # if curr.month == 8 and curr.day == 23:
                #     print('it is my birthday!')
                cnt += 1
            #print(ds)
            curr += timedelta(days=1)
        duration = time() - start
        print(f'from {start_d} to {end_d}, there are {cnt} prime days')
        show_duration(duration)

def main():
    ''' main '''
    td = TestDate()
    #td.test('20190823')
    td.run()

if __name__ == '__main__':
    main()
