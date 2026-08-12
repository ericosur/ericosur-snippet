#!/usr/bin/env python3

'''
demo of typer with datetime argument
it is a similar version of ep.py

since it is called "[a-z]+_typer.py", the typer is required
'''

import sys
from datetime import datetime, timezone
from typing import Annotated

try:
    import typer
except ImportError as e:
    print("FAIL to import:", e)
    sys.exit(1)

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]},
                  help="epoch / timestamp utility",
                  no_args_is_help=True)

try:
    from datetime_common import do_nothing
    from ep import datetime2epoch, epoch2timestr
except ImportError as e:
    print("fail to import:", e)
    sys.exit(1)


def run_demo() -> None:
    ''' demo '''
    msg = '''===== timestamp / epoch demo =====\n
# get currect timestamp:
/usr/bin/date +%s
# python one-liner
py -c "import time; print(int(time.time()))"

# get specific timestamp from datetime
/usr/bin/date +%s -d"2022-07-08 17:08:00"
# call this script by:
python date_typer.py --datetime 2022-07-08T17:08:00
python date_typer.py --epoch 1735101296
'''
    print(msg)
    print("demo...")
    dt = "2024-12-25 12:34:56"
    ep = datetime2epoch(dt)
    print(ep)
    ts = epoch2timestr(ep)
    print(ts[1])

@app.command()
def main(
    dateval: Annotated[
        datetime | None,
        typer.Option("--datetime", "--date", "-D",
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    ] = None, #"1970-01-01T00:00:00",
    numval: Annotated[int | None, typer.Option("--epoch", "--number", "-e",
        help="epoch value in number")] = None, # 1234567890
    debug: Annotated[bool, typer.Option("--debug", help="turn on debug")] = False,
    human: Annotated[bool, typer.Option("--human", "-H", help="human read flag")] = False,
    demo: Annotated[bool, typer.Option("--demo", help="get some demo")] = False,
    now: Annotated[bool, typer.Option("--now", "-n", help="use current local time as input")] = False,
    utc: Annotated[bool, typer.Option("--utc/--local", "-u/-l", help="UTC (default) or local timezone")] = True,
) -> None:
    '''
    epoch / timestamp demo
    '''
    logd = do_nothing
    if debug:
        logd = print

    if demo:
        run_demo()
        return

    tz_label = 'UTC' if utc else 'local'

    if now:
        dateval = datetime.now().astimezone()

    if dateval:
        # human date string to epoch
        logd(f'{dateval=}')
        logd(f'may also use: date +%s -d"{dateval}"')
        if utc:
            ts = int(dateval.replace(tzinfo=timezone.utc).timestamp())
        else:
            ts = int(dateval.astimezone().timestamp())
        print(f'{ts} ({tz_label})')
        return
    if numval:
        # epoch to date string
        ret = epoch2timestr(numval, human=human, utc=utc)
        logd(ret)
        logd(f"may also use: date -R -d '@{numval}'")
        print(f'{ret[1]} ({tz_label})')
        return
    print('get some help, use "--help"')

if __name__ == "__main__":
    #typer.run(main)
    app()
