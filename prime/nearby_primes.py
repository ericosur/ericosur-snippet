#!/usr/bin/python3
# coding: utf-8

'''
given cli argument to get lower/upper prime

'''

import sys
import random
from lcp import LoadCompressPrime

# pylint: disable=invalid-name
def test(argv, sp):
    ''' test '''
    print(sp)

    if argv == []:
        _max = sp.at(sp.get_count() - 1)
        _min = sp.at(0)
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 1
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
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

def main(argv):
    ''' main function '''
    with LoadCompressPrime() as sp:
        test(argv, sp)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except IndexError:
        print('specify numbers to search nearby primes')
