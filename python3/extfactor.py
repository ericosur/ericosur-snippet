#!/usr/bin/env python3
# coding: utf-8

'''
    call /usr/bin/factor and pick results
    also refer to **factorint.py** that uses sympy to do factorize
'''

import argparse
import os
import re
import sys
import time
from random import randint
from myutil import read_from_stdin, isfile

def is_positive_integer(the_input):
    """ Checks if a number is a positive integer.
    Args:
      the_input: The number to check.
    Returns:
      True if the number is a positive integer, False otherwise.
    """
    if isinstance(the_input, int):
        return the_input > 0

    if isinstance(the_input, str):
        try:
            # Attempt to convert the input to an integer
            number_as_int = int(the_input)
            return number_as_int > 0
        except ValueError:
            # If conversion fails (not a number), return False
            return False

    if isinstance(the_input, float):
        r = round(the_input)
        return r == the_input and r > 0

    return False

class Solution():
    ''' call external factor to do factorize '''
    THE_CMD = '/usr/bin/factor'

    def __init__(self):
        self.__check_execute()

    def __check_execute(self):
        ''' return true if the fn exists '''
        if not isfile(Solution.THE_CMD):
            print(f'[fail] not found: {Solution.THE_CMD}')
            sys.exit()

    def call_factor(self, n: int):
        ''' call external factor '''
        cmd = f'{Solution.THE_CMD} {n}'
        a = os.popen(cmd).read()
        #print(res)
        b = re.sub(r'^(\d+: )(.+)$', '\\2', a.strip())
        vals = b.split(' ')
        print(f'{n}: ', end='')
        if len(vals) == 1:
            print('a prime number')
        else:
            print(vals)

    def action(self, the_list):
        ''' action '''
        for v in the_list:
            if is_positive_integer(v):
                self.call_factor(v)
            else:
                print(f'invalid input: {v}')

    @classmethod
    def run(cls, the_list):
        ''' run me '''
        obj = cls()
        obj.action(the_list)

def process_list(args):
    ''' process or prepare the list '''
    if args == []:
        print('demo: add some samples...')
        args.append(time.time())
        for _ in range(3):
            args.append(randint(946656000, 1609344000))

    Solution.run(args)


def main():
    ''' main '''
    # prepare and parse CLI arguments
    parser = argparse.ArgumentParser(description='factor specified numbers',
        epilog='try: extfactor.py 3628800')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', type=int, default=None)
    args = parser.parse_args()
    #print(args)
    if args.readFromStdin:
        read_from_stdin(process_list)
    else:
        process_list(args.arg)

if __name__ == '__main__':
    main()
