#!/usr/bin/python3
# coding: utf-8

'''
testing LoadCompressPrime/store_prime
'''

try:
    # larger and slower
    from sip import LoadCompressPrime as StorePrime
    print('use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker
    from store_prime import StorePrime
    print('use **store_prime**')

def gold_bach(val):
    ''' it could be found if val < 4 * 10^17 '''
    print(f'test: {val}')
    max_len = 12

    with StorePrime() as sp:
        ret = sp.get_primes_less_than(val)
        if isinstance(ret, list):
            if len(ret) > max_len:
                print(f"got a list which size is more than {max_len}")
            else:
                print(ret)

def main():
    ''' main '''
    gold_bach(500)

if __name__ == '__main__':
    main()
