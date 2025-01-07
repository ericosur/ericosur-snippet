#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
provide a function to run command, fetch the output,
and return as a list of strings for further parsing
'''

import subprocess
import sys
from sysconfig import get_platform
from typing import Union
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

def is_linux() -> bool:
    ''' check if running on Linux '''
    return "linux" in get_platform()

def is_cygwin() -> bool:
    ''' check if cygwin '''
    return "cygwin" in get_platform()

def is_windows() -> bool:
    ''' has win in the platform string
        will meet cygwin and win-amd64
    '''
    return "win" in get_platform()

def show_platform() -> None:
    ''' show platform '''
    prt(f'platform: {get_platform()}')

def run_command(cmd: str) -> Union[list[str], None]:
    ''' run specified command and return the output
        note: will exit app if error occurs
    '''
    outs = None
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True) as p:
        try:
            # due to "text=True", the type is str, str
            stdout, stderr = p.communicate()
            if p.returncode != 0:
                sout = stderr.strip()
                prt(f"Error: {sout}")
                sys.exit(1)
            outs = stdout.splitlines()
        except UnicodeDecodeError as err:
            prt(f"Error: {err}")
    return outs


def run_command2(cmd: str) -> Union[list[str], None]:
    ''' run specified command and return the output
        decoding with cp950 (traditional chinese)
        note: will exit app if error occurs
    '''
    outs = None
    CP = "cp950"  # for Windows TC
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as p:
        result = ""
        try:
            # cannot use text=True under Windows (non-en locale)
            stdout, stderr = p.communicate()  # bytes, bytes

            if p.returncode != 0:
                err_out = stderr.decode(CP)
                prt(f"Error: {err_out}")
                sys.exit(1)

            result = stdout.decode(CP)
        except UnicodeDecodeError as err:
            prt(f"Error: {err}")
    outs = result.splitlines()
    return outs


if __name__ == "__main__":
    prt(f'{sys.argv[0]} is a module, not a standalone script')
    sys.exit(1)
