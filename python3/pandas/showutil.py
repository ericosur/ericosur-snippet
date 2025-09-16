#!/usr/bin/env python3
# coding: utf-8

''' some useful functions to show data '''

try:
    from rich.table import Table
    from rich.console import Console
    USE_TABLE = True
except ImportError:
    print('[FAIL] rich module not found, install with pip3 install rich')
    USE_TABLE = False

from working_days import LoadWorkingDays
from strutil import str2sec

BASIC_KEYS = ['max', '75%', 'mean', '50%', '25%', 'min', 'std']
EXT_KEYS = ['max', '99%', '95%', '90%', '75%', 'mean', '50%', '25%', 'min', 'std']

def print_sep():
    ''' print seperator '''
    print('-' * 50)

def show_curios():
    ''' show some readme '''
    msg = '''
# some curios for normal distribution (only right side of μ)
0~1σ = 34.1%
1σ~2σ = 13.6% (acc: 47.7%, ±2σ: 95.4%)
2σ~3σ = 2.1%  (acc: 49.8%, ±4σ: 99.6%)
3σ~   = 0.1%  (acc: 49.9%)
'''
    print(msg)

def show_extra_header(the_output) -> None:
    ''' show extra header '''
    print(f'[INFO]    first date: {the_output["first"]}')
    print(f'[INFO]     last date: {the_output["last"]}')
    print(f'[INFO]   during days: {the_output["during"]}')

def show_workingdays(verbose: bool) -> None:
    ''' show working days '''
    if not verbose:
        return
    lower = 2021
    upper = 2024
    wd = LoadWorkingDays()
    for y in range(lower, upper+1):
        print(wd.get_msg(y))

def show_simplecsv(outputs):
    ''' csv output '''
    for k,v in outputs.items():
        print(f'"{k}", "{v}"')

def show_outputs(outputs, logd, logi, use_extended=False):
    ''' show the ouput
        if module rich is installed, will use rich.table,
        else use simple text
        note: may override the flag to debug
    '''
    # if flag is on, will not use rich.table
    # or conside table.rich is installed or not
    OVERRIDE_FLAG = False
    print_sep()
    if USE_TABLE and not OVERRIDE_FLAG:
        __show_outputs_table(outputs, logd, logi, use_extended=use_extended)
    else:
        __show_outputs_text(outputs, logd, logi, use_extended=use_extended)
        print_sep()

def __show_outputs_text(outputs, logd, logi, use_extended=False):
    ''' show outputs '''
    if use_extended:
        text_keys = ['count', *EXT_KEYS]
    else:
        text_keys = ['count', *BASIC_KEYS]
    for k in text_keys:
        v = outputs[k]
        if k == "count":
            result = v
            j = result.rjust(9, ' ')
        else:
            try:
                secs = str2sec(v)
                result = f'{v}  ({secs:4.0f})'
                j = result.rjust(20, ' ')
            except ValueError:
                logd(f'[FAIL] at {k=} {v=}')
                logi('[INFO] some data line is incorrect,',
                        'download the csv and run ```check_csv.py```')
                continue
        print(f'{k:10s}: {j:20s}')

def __show_outputs_table(outputs, logd, logi, use_extended=False):
    ''' show outputs with rich.table '''
    console = Console()
    table = Table(title="Statistics")
    table.add_column("Items", justify="left", style="cyan")
    table.add_column("Value", justify="right", style="magenta")
    table.add_column("Sec", justify="right", style="green")
    # first row for count
    item = 'count'
    value = outputs.get(item)
    table.add_row(item, value, '')
    # 2nd rows and later
    the_keys = EXT_KEYS if use_extended else BASIC_KEYS
    for k in the_keys:
        item = k
        value = outputs.get(k)
        try:
            sec_float = str2sec(value)
            sec_text = f'{sec_float:4.0f}'
            table.add_row(item, value, sec_text)
        except ValueError:
            logd(f'[FAIL] at {k=} {value=}')
            logi('[INFO] some data line is incorrect,',
                    'download the csv and run ```check_csv.py```')
            continue
    console.print(table)
