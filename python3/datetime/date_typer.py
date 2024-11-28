#!/usr/bin/env python3
#coding: utf-8

'''
demo of typer with datetime argument
'''

from datetime import datetime
import typer
from typing_extensions import Annotated, Any

from ep import epoch2timestr, datetime2epoch

# pylint: disable=unused-argument
def do_nothing(*args: Any) -> None:
    ''' do nothing '''
    return

def main(
    dateval: Annotated[
        datetime,
        typer.Option("--datetime", "--date", "-D",
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    ] = None, #"1970-01-01T00:00:00",
    numval: Annotated[int, typer.Option("--epoch", "--number", "-e", "-n",
        help="epoch value in number")] = None, # 1234567890
    debug: Annotated[bool, typer.Option("--debug", help="turn on debug")] = False,
    human: Annotated[bool, typer.Option("--human", help="turn on debug")] = False,
    demo: Annotated[bool, typer.Option("--demo", help="get some demo")] = False
):
    '''
    epoch / timestamp demo
    '''
    logd = do_nothing
    if debug:
        logd = print

    if demo:
        msg = '''===== timestamp / epoch demo =====\n
# get currect timestamp:
/usr/bin/date +%s
# python one-liner
py -c "import time; print(int(time.time()))"

# get specific timestamp from datetime
/usr/bin/date +%s -d"2022-07-08 17:08:00"
# call this script by:
python date_typer.py --datetime 2022-07-08T17:08:00
'''
        print(msg)
        dt = "2022-07-08 17:08:00"
        ret = datetime2epoch(dt)
        return
    if dateval:
        # human date string to epoch
        # date +%s -d"Jan 1, 1980 00:00:01"
        logd(f'{dateval=}')
        logd(f'may also use: date +%s -d"{dateval}"')
        ts = int(dateval.timestamp())
        print(ts)
        return
    if numval:
        # epoch to date string
        # date -d @1520000000
        ret = epoch2timestr(numval, human=human)
        logd(ret)
        logd(f"may also use: date -R -d '@{numval}'")
        print(ret[1])
        return
    print('get some help, use "--help"')

if __name__ == "__main__":
    typer.run(main)
