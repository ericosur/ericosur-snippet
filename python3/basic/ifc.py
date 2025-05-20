#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call ifconfig and parse the output
'''

import os
import re
import sys
try:
    #from rich import print as pprint
    from rich.pretty import pprint
    from rich.console import Console
    from rich.table import Table
    RICH_ENABLED = True
    prt = pprint
    console = Console()
    logd = console.log
except ImportError:
    prt = print
    logd = print
    RICH_ENABLED = False

from read_os_release import is_ubuntu1804

# ruff: noqa: E402
sys.path.insert(0, './')
sys.path.insert(0, '../')
sys.path.insert(0, 'python3/')
from myutil import is_linux, is_windows, show_platform  # type: ignore[import]
from myutil import run_command, run_command2  # type: ignore[import]

def run_in_termux() -> bool:
    ''' get prefix '''
    p = os.environ.get('PREFIX')
    if p is None:
        return False
    p = p.decode('utf-8')
    return "com.termux" in p

def run_ipconfig() -> None:
    ''' run ipconfig (in cygwin/windows) '''
    outs = run_command2("ipconfig")
    if outs is None:
        return
    reg1 = r'^(\S+ .+):'
    reg2 = r'\s+IPv4.+\s+:\s+(\S+)'
    ifn, ipaddr = "", ""
    for ln in outs:
        m1 = re.search(reg1, ln)
        if m1:
            ifn = m1.group(1)
            continue
        m2 = re.search(reg2, ln)
        if m2:
            ipaddr = m2.group(1)
            prt(f'{ifn}: {ipaddr}')

def get_ipaddr() -> list[dict[str,str]] | None:
    ''' get ip addr via ifconfig '''
    # only change path of ifconfig for known ubuntu 18.04
    cmd = "/sbin/ifconfig" if is_ubuntu1804() else "/usr/sbin/ifconfig"
    if not os.path.exists(cmd):
        logd(f"file not found: {cmd}")
        cmd = 'ifconfig'
    outs = run_command(cmd)
    if outs is None:
        return None
    reg1 = r'^(\S+):'
    reg2 = r'inet\s+(\S+)\s+netmask\s+(\S+)'
    reg3 = r'ether\s+(\S+)\s+'
    rets = []
    tmp = {}
    for ln in outs:
        ln = ln.strip()
        m1 = re.search(reg1, ln)
        if m1:
            ifn = m1.group(1)
            tmp['interface'] = ifn
            continue
        m2 = re.search(reg2, ln)
        if m2:
            tmp['inet'] = m2.group(1)
            #tmp['netmask'] = m2.group(2)
            continue
        m3 = re.search(reg3, ln)
        if m3:
            tmp['MAC'] = m3.group(1)
        if tmp:
            rets.append(tmp)
        tmp = {}
    # go throught rets, remove the dict that has no inet
    rets = [d for d in rets if 'inet' in d]
    return rets

def show_as_table(ret: list[dict[str,str]]) -> None:
    ''' show as table '''
    table = Table(title="IP Address")
    table.add_column("interface", justify="left", style="cyan")
    table.add_column("inet", justify="left", style="magenta")
    table.add_column("MAC", justify="left", style="green")
    for d in ret:
        ifn = d.get('interface', '')
        inet = d.get('inet', '')
        mac = d.get('MAC', '')
        table.add_row(ifn, inet, mac)
    console.print(table)

def main():
    ''' main '''
    if is_linux():
        # note: if returns has no inet, it will be removed
        ret = get_ipaddr()
        if RICH_ENABLED:
            show_as_table(ret)
        else:
            prt(ret)
    elif is_windows():
        run_ipconfig()
    else:
        prt('this script is for Linux only')
        show_platform()

if __name__ == "__main__":
    main()
