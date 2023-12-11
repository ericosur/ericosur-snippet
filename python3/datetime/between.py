#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
datetime sample
'''

from __future__ import print_function

from datetime import datetime, timedelta


def main():
    ''' main function '''
    #ww = [8, 30]
    ww = [9, 21]
    # here is time I enter workspace
    from_time = datetime.now().replace(hour=ww[0], minute=ww[1], second=0, microsecond=0)
    print('from_time:', from_time)

    # current time
    now_time = datetime.now().replace(microsecond=0)
    print('now_time: ', now_time)

    most_early_time = datetime.now().replace(hour=17, minute=30, second=0, microsecond=0)
    #print most_early_time

    # need more than work_hour
    work_hour = timedelta(hours=9)


    if now_time - from_time > work_hour:
        print("ok, long enough")
    else:
        real_work_hour = from_time + work_hour
        real_work_hour = max(real_work_hour, most_early_time)
        print("+++++ should be:", real_work_hour)
        diff_hour = real_work_hour - now_time
        print(f'diff: {diff_hour}')


if __name__ == '__main__':
    main()
