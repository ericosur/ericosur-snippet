#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call ifconfig and parse the output
'''

import os
import re
import sys
from rich import print as rprint
prt = rprint
from run_cmd import run_command, run_command2
from run_cmd import is_linux, is_cygwin, show_platform
from read_os_release import is_ubuntu1804

def run_ipconfig():
    ''' run ipconfig (in cygwin/windows) '''
    outs = run_command2("ipconfig")
    reg1 = r'^(\S+ .+):'
    reg2 = r'\s+IPv4.+\s+:\s+(\S+)'
    for ln in outs:
        m1 = re.search(reg1, ln)
        if m1:
            ifn = m1.group(1)
            continue
        m2 = re.search(reg2, ln)
        if m2:
            ipaddr = m2.group(1)
            prt(f'{ifn}: {ipaddr}')

def get_ipaddr() -> dict:
    ''' get ip addr via ifconfig '''
    # only change path of ifconfig for known ubuntu 18.04
    cmd = "/sbin/ifconfig" if is_ubuntu1804() else "/usr/sbin/ifconfig"
    if not os.path.exists(cmd):
        prt(f"file not found: {cmd}")
        sys.exit(1)
    outs = run_command(cmd)
    reg1 = r'^(\S+):'
    reg2 = r'inet\s+(\S+)\s+netmask\s+(\S+)'
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
        if tmp:
            rets.append(tmp)
        tmp = {}
    return rets

def main():
    ''' main '''
    if is_linux():
        prt(get_ipaddr())
    elif is_cygwin():
        run_ipconfig()
    else:
        prt('this script is for Linux only')
        show_platform()

if __name__ == "__main__":
    main()
