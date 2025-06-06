#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=wrong-import-position
#

'''
convert epoch value to date/time string

reference:
https://www.epochconverter.com/

python:
import calendar, time
calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))
# as the following

import time
time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
# Replace time.localtime with time.gmtime for GMT time.
# Or using datetime:
import datetime
datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)


## tips
linux shell:
# Replace '-d' with '-ud' to input in GMT/UTC time
# human date string to epoch
date +%s -d"Jan 1, 1980 00:00:01"
# epoch to date string
date -d @1520000000

## in my own git repository, also see:
https://github.com/ericosur/ericosur-snippet/blob/master/shell/date-string-example.sh
https://github.com/ericosur/ericosur-snippet/tree/master/root/epoch

'''

import argparse
import calendar
import sys
import time
from random import randint
from typing import Tuple

sys.path.insert(0, '..')
sys.path.insert(0, 'python3')
from myutil import read_from_stdin  # type: ignore[import]

def datetime2epoch(date_str: str) -> int:
    ''' given datetime string (YYYY-MM-DD HH:MM:SS)
        return epoch
    '''
    return calendar.timegm(time.strptime(date_str, '%Y-%m-%d %H:%M:%S'))

def epoch2timestr(epoch: int, human: bool=False) -> Tuple[int, str]:
    ''' Replace time.localtime with time.gmtime for GMT time '''
    if epoch == -1:
        epoch = int(time.time())

    msg = ""
    if human:
        msg = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))
    else:
        msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch))
    return (epoch, msg)


def main(args: list):
    ''' main '''
    if args == []:
        print('apply sample numbers...')
        args.append(time.time())
        args.append(172162800)
        for _ in range(3):
            args.append(randint(946656000, 1609344000))

    for v in args:
        try:
            num = int(v)
            print(epoch2timestr(num))
        except ValueError:
            print(f'{v} is not a valid integer')

def argp() -> None:
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='convert epoch value to date/time string',
        epilog='try ```$(date +%s)``` as argument')
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', type=int, default=None)
    args = parser.parse_args()
    #print(args)
    if args.readFromStdin:
        read_from_stdin(main)
    else:
        main(args.arg)

if __name__ == "__main__":
    argp()
