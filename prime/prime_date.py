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
'''

from datetime import date, timedelta

# try to import StorePrime class
try:
    # larger and slower for loading pickle
    from sip import LoadCompressPrime as StorePrime
    print('use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker for loading pickle
    from store_prime import StorePrime
    print('use **store_prime**')


# pylint: disable=invalid-name
# too-many-statements

class TestDate():
    ''' test date is a prime '''
    def __init__(self):
        self.sp = StorePrime()
        self.sp.load_pickle()

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
            print('{} is a prime day!'.format(argv))
        return allprime

    def run(self):
        ''' run '''
        start_d = date(2001, 1, 1)
        end_d = date(2099, 12, 31)
        curr = start_d
        cnt = 0
        while curr <= end_d:
            ds = curr.strftime('%Y%m%d')    # 20190823
            if self.test(ds):
                # if curr.month == 8 and curr.day == 23:
                #     print('it is my birthday!')
                cnt += 1
            #print(ds)
            curr += timedelta(days=1)
        print('from {} to {}, there are {} prime days'.format(start_d, end_d, cnt))

def main():
    ''' main '''
    td = TestDate()
    #td.test('20190823')
    td.run()

if __name__ == '__main__':
    main()
