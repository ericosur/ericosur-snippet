#!/usr/bin/env python3

'''
datetime sample
'''


from datetime import datetime, timedelta

from be_prepared import get_current_taipei_datetime


def get_current_datetime() -> datetime:
    ''' get current datetime '''
    return get_current_taipei_datetime()

def main():
    ''' main function '''
    ww = [8, 30]
    #ww = [9, 21]
    # here is time I enter workspace
    from_time = get_current_datetime().replace(hour=ww[0], minute=ww[1], second=0, microsecond=0)
    print('from_time:', from_time)

    # current time
    now_time = get_current_datetime().replace(microsecond=0)
    print('now_time: ', now_time)

    most_early_time = get_current_datetime().replace(hour=17, minute=30, second=0, microsecond=0)
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
