#!/usr/bin/env python3
# coding: utf-8

'''
use method of 'sieve of eratosthenes' to get four-digit-primes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

there is a speed-upgraded version 'sieve.py'
'''

def output_to_file(fn, primes):
    ''' output list into text file '''
    with open(fn, "wt", encoding='utf8') as ofh:
        for pp in primes:
            ofh.write(f"{pp}\n")
    print(f'output to {fn}, count = {len(primes)}')

def main():
    ''' main '''
    small_primes = [2, 3, 5, 7, 11,
                    13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97]
    LOWER = 2
    UPPER = 100000
    print(f'integers from {LOWER} to {UPPER-1}')
    target = list(range(LOWER, UPPER))
    for pp in small_primes:
        cnt = 0
        print(f'use {pp} to filter, count {len(target)} before start ', end='')
        for nn in target:
            if nn % pp == 0:
                cnt += 1
                target.remove(nn)
        print(f"removed: {cnt}, left: {len(target)}")

    print("end...")
    print("left count of numbers:", len(target))

    # uncomment the following line if output to file
    #output_to_file('primes_need_check.txt', target)


if __name__ == '__main__':
    print('there is also a speed-upgraded version: sieve.py')
    main()
