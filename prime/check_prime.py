#!/usr/bin/env python3
# coding: utf-8

'''
check if input number is prime or not
support read lines from stdin

eg:
# pick from file
shuf -n 10 large.txt | python3 check_prime.py -

# random generate (range from 1001 to 9999)
shuf -i 1001-9999 -n 10 | python3 check_prime.py -

'''

import sys
try:
    import sympy
except ImportError:
    print('need install module **sympy**')
    sys.exit()

def is_prime(n: int):
    ''' check if a prime with sympy '''
    return sympy.ntheory.primetest.isprime(n)

def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    main(args)

def main(argv: list):
    ''' main '''
    if argv == []:
        print('no item in list')
    else:
        for e in argv:
            try:
                m = int(e)
                ret = is_prime(m)
                print('{} is '.format(m), end='')
                if ret:
                    print('a PRIME')
                else:
                    print('NOT a prime')

            except ValueError:
                print('value error: {}'.format(m))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin()
        else:
            main(sys.argv[1:])
    else:
        print('use "{} -"'.format(sys.argv[0]))
