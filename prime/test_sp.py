#!/usr/bin/env python3
# coding: utf-8

'''
test StorePrime
'''

import random
from myutil import read_setting
from store_prime import StorePrime
from sip import LoadCompressPrime


def test(argv, sp):
    ''' test '''
    print(sp)
    #rint(sp.get_count())

    if argv == []:
        _max = sp.at(sp.get_count() - 1)
        _min = sp.at(0)
        #print("max:{}, min:{}".format(_max, _min))
        REPEAT = 10
        for _ in range(REPEAT):
            r = random.randint(_min, _max)
            argv.append(r)

    for ss in argv:
        try:
            val = int(ss)
            sp.test(val)
        except ValueError:
            print('    {} is a ValueError'.format(ss))
            continue


def main(argv, item):
    ''' main function '''
    data = read_setting('setting.json')
    txtfn = data['prime_large']
    pfn = data['pickle_large']
    print(txtfn, pfn)

    if item == 'sp':
        with StorePrime(txtfn, pfn) as sp:
            test(argv, sp)
    else:
        with LoadCompressPrime() as sp:
            test(argv, sp)


if __name__ == '__main__':
    import sys

    try:
        if sys.argv[1] in ('sp', 'sip'):
            main(sys.argv[2:], sys.argv[1])
    except IndexError as err:
        print(err)
        print('specify arg: sp or sip')
