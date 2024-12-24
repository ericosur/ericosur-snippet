#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
provide a function to run command, fetch the output,
and return as a list of strings for further parsing
'''

import subprocess
import sys
from sysconfig import get_platform
from typing_extensions import List, Optional
from rich import print as rprint
prt = rprint

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

def run_command(cmd: str) -> Optional[List[str]]:
    ''' run specified command and return the output
        note: will exit app if error occurs
    '''
    outs = None
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True) as p:
        try:
            stdout, stderr = p.communicate()

            if p.returncode != 0:
                prt(f"Error: {stderr.strip()}")
                sys.exit(1)

            outs = stdout.splitlines()

        except UnicodeDecodeError as err:
            prt(f"Error: {err}")

    return outs


def run_command2(cmd: str) -> Optional[List[str]]:
    ''' run specified command and return the output
        decoding with cp950 (traditional chinese)
        note: will exit app if error occurs
    '''
    outs = None
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as p:
        try:
            stdout, stderr = p.communicate()

            if p.returncode != 0:
                prt(f"Error: {stderr.strip()}")
                sys.exit(1)

            stdout = stdout.decode("cp950")
        except UnicodeDecodeError as err:
            prt(f"Error: {err}")
    outs = stdout.splitlines()
    return outs


if __name__ == "__main__":
    prt(f'{sys.argv[0]} is a module, not a standalone script')
    sys.exit(1)
