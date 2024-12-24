#!/usr/bin/env python3
#coding: utf-8

'''
demo of typer with datetime argument
it is a similar version of ep.py

since it is called "[a-z]+_typer.py", the typer is required
'''

from datetime import datetime
import sys
from typing_extensions import Annotated
try:
    import typer
except ImportError as e:
    print("FAIL to import:", e)
    sys.exit(1)

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]},
                  help="epoch / timestamp utility",
                  no_args_is_help=True)

sys.path.insert(0, "..")
sys.path.insert(0, "datetime")
sys.path.insert(0, "myutil")
sys.path.insert(0, "python3/datetime")
from ep import epoch2timestr, datetime2epoch

# pylint: disable=unused-argument
def do_nothing(*args) -> None:
    ''' do nothing '''
    return

def run_demo():
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
        datetime,
        typer.Option("--datetime", "--date", "-D",
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    ] = None, #"1970-01-01T00:00:00",
    numval: Annotated[int, typer.Option("--epoch", "--number", "-e", "-n",
        help="epoch value in number")] = None, # 1234567890
    debug: Annotated[bool, typer.Option("--debug", help="turn on debug")] = False,
    human: Annotated[bool, typer.Option("--human", "-H", help="human read flag")] = False,
    demo: Annotated[bool, typer.Option("--demo", help="get some demo")] = False
):
    '''
    epoch / timestamp demo
    '''
    logd = do_nothing
    if debug:
        logd = print

    if demo:
        run_demo()
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
    #typer.run(main)
    app()
