#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo days delta
'''

from datetime import datetime, timedelta
from typing import Union, Annotated
try:
    import typer
    USE_TYPER = True
except ImportError:
    print('warn: cannot imort typer, run demo only...')
    USE_TYPER = False

def translate_weekday(w: int) -> int:
    '''
    in module datetime, return value of d.weekday() monday is 0, sunday is 6
    translate it to sunday = 0, monday = 1, ..., saturday = 6
    '''
    if 0 <= w <= 6:
        t = w + 1
        t = t % 7
        return t
    raise ValueError("value out of range")

def get_date_after_days(start_date: datetime, offset_days: int) -> datetime:
    ''' given start date and offset days, return new datetime obj '''
    # define offset
    offset = timedelta(days=offset_days)
    new_date = start_date + offset
    return new_date

def demo_only() -> None:
    '''demo function'''
    print("demo...")
    start = datetime.today()
    delta = 60
    get_result(start, delta)

def get_result(start: datetime, delta: int) -> None:
    ''' calculate date and show result '''
    # for datetime
    wd_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # if translated
    #tws = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    nd = get_date_after_days(start, delta)
    wd = wd_name[nd.weekday()]
    print(f'since {start}, weekday is {wd_name[start.weekday()]}')
    print(f'after {delta} days, it is {nd} and weekday is {wd}')

if USE_TYPER:
    def main(
        dateval: Annotated[
            Union[datetime, None],
            typer.Option("--datetime", "--date", "-D",
                formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
        ] = None, #"1970-01-01T00:00:00",
        numval: Annotated[int, typer.Option("--delta", "--between", "--offset",
            help="epoch value in number")] = 30, # 1234567890
        demo: Annotated[bool, typer.Option("--demo", help="get some demo")] = False
    ):
        '''
        datedelta demo, for example

        new_date.py -D 1946-06-14T12:34:56 --offset 28490
        '''
        if demo:
            demo_only()
            return
        if dateval is None:
            print('error: MUST specify a date string')
            print('get some help: --help')
            return
        get_result(dateval, numval)

if __name__ == '__main__':
    if USE_TYPER:
        typer.run(main)
    else:
        demo_only()
