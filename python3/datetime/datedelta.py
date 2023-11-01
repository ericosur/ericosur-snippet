#!/usr/bin/env python3

'''
datetime delta
'''

from datetime import timedelta, datetime
import math
import operator

def main():
    ''' main '''
    start = datetime(1975, 6, 17, 12, 0, 0)
    print("start date:", start)
    today = datetime.today()
    print('diff since start:', today - start)

    deltas = {'10**9': timedelta(seconds=1e9),
              '2.0 * 10**9': timedelta(seconds=2e9),
              '1.5 * 10**9': timedelta(seconds=1.5e9),
              '2**30': timedelta(seconds=2**30),
              '10**21': timedelta(seconds=math.exp(21)),
              '2**31': timedelta(seconds=math.pow(2, 31)),
              '10**22': timedelta(seconds=math.exp(22))}
    # sort arr by value
    sorted_v = sorted(deltas.items(), key=operator.itemgetter(1))
    for (k, v) in sorted_v:
        result = start + v
        print(f'add {k:12s}: {result}')


if __name__ == '__main__':
    main()
