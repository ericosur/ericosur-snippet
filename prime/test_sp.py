#!/usr/bin/env python3
# coding: utf-8

'''
test StorePrime
'''


def test(argv, sp):
    ''' test '''
    import random

    print(sp)
    #print(sp)
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
    if item == 'sp':
        from store_prime import StorePrime
        with StorePrime() as sp:
            test(argv, sp)
    else:
        from sip import LoadCompressPrime
        with LoadCompressPrime() as sp:
            test(argv, sp)


if __name__ == '__main__':
    import sys

    try:
        if sys.argv[1] in ('sp', 'sip'):
            main(sys.argv[2:], sys.argv[1])
    except IndexError:
        print('**python3 test_sp.py sp**  OR')
        print('**python3 test_sp.py sip**')
