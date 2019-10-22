#!/usr/bin/env python3

'''
datetime delta
'''

# pylint: disable=blacklisted-name

from datetime import timedelta, datetime
import math

def main():
    ''' main '''
    foo = datetime.datetime(1975, 6, 17, 12, 0, 0)
    print("start date:", foo)

    arr = [
        timedelta(seconds=1e9),
        timedelta(seconds=2**30),
        timedelta(seconds=math.exp(21))
        ]
    for delta in arr:
        #print 'delta:', delta
        bar = foo + delta
        print(bar)

    # offset = timedelta(seconds=2**30)
    # print offset

    # foo += offset
    # print foo

if __name__ == '__main__':
    main()
