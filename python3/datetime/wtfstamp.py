#!/usr/bin/env python3
#coding: utf-8

'''

https://www.reddit.com/r/AutoHotkey/comments/1f68ref/steam_timestamps/
https://stackoverflow.com/questions/58398993/how-to-convert-a-really-long-timestamp-into-datetime-19-digits-98764321012345

timestamp = 5249845694418721250;
Ends up August 21, 2024 @ 8:36pm

timestamp = 5250289887910686546;
Ends up August 27, 2024 @ 1:22pm

IEEE 754
1 bit for the sign (positive or negative)
11 bits for the exponent
52 bits for the significand (also known as the mantissa)

'''

from datetime import datetime
import time

from sickutil import logv, loge, get_sick_from_ns
from sickutil import sick_to_ns, sick_to_datetime, datetime_to_sick

class Solution():
    ''' solution '''
    def __init__(self):
        self.min_epoch = 0
        self.max_epoch = 0

    def get_range(self):
        ''' get range '''
        dt1 = datetime(2024,8,21,0,0,0)
        self.min_epoch = dt1.timestamp()
        dt2 = datetime(2024,8,29,23,59,59)
        self.max_epoch = dt2.timestamp()

    def process_values(self, vals: list[int]):
        ''' process values '''
        for v in vals:
            if len(str(v)) != 19:
                loge('ERROR: the length is incorrect', v)
            sick_to_datetime(v)

    def check(self, *args):
        ''' input args of sick number, get datetime from sick '''
        for i in args:
            sick_to_datetime(i)

    def action(self):
        ''' action '''
        self.get_range()
        try:
            vals = [5020107264551401283, 5249845694418721250, 5250289887910686546]
            self.process_values(vals)
        except OverflowError as e:
            logv(e)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def output_for_five_head(ns, sick, dt, cnt, ns_val):
    ''' output for five head '''
    print()
    print(f'  {sick=} ({len(str(sick))})')
    print(f'    {ns=}')
    print(f'    {dt=}')
    print(f'{ns_val=}')
    diff = abs(ns_val-ns)
    print(f'  {diff=}, {cnt=}')

def look_for_five_head() -> None:
    ''' look for five head from now
        For time_ns(), it looks like a sequence number. It is possible that
        the first 5 digits are all the same within a day. The sick number
        will provide a confusing value from a normal epoch.

        It does not match one-by-one for ns vs sick. The floating number has
        some rounding errors or effective digits issue. For example,
        call get_sick_from_ns(ns=1725349461401815114) will get
        sick=5207463204362499907, but sick_to_ns() WILL NOT get the same
        ns value.

        check
        need pass this: ns=1725351036589899672
        OK ns=1725350935165748837
    '''
    LOOK_FOR_FIVE_HEAD = True
    cnt = 0
    while LOOK_FOR_FIVE_HEAD:
        ns = time.time_ns()
        #ns=1725351036589899672
        #ns=1725350935165748837
        print(f'{ns}\r', end='')
        sick = get_sick_from_ns(ns)
        cnt += 1
        if str(sick)[0] == '5':
            dt = sick_to_datetime(sick)
            ns_val = sick_to_ns(sick)
            output_for_five_head(ns, sick, dt, cnt, ns_val)
            break
        time.sleep(0.25)

def look_for_1e9() -> None:
    ''' 1e9 loop '''
    obj = Solution()
    d1 = datetime_to_sick(datetime(2024, 8, 21, 20, 36))
    #d2 = datetime_to_sick(datetime(2024, 8, 27, 13, 22))
    for i in range(1, 1_000_000_000):
        obj.check(d1+i)

def main():
    ''' main '''
    look_for_five_head()

if __name__ == '__main__':
    main()
