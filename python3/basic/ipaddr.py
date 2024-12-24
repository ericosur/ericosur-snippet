#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call __ip addr__ and parse
'''

import re
import sys
from rich import print as rprint
prt = rprint
from run_cmd import run_command, is_linux
from read_os_release import is_ubuntu1804

def get_ipaddr() -> dict:
    ''' get ip addr'''
    cmd = "/sbin/ip addr" if is_ubuntu1804() else "/usr/sbin/ip addr"
    outs = run_command(cmd)

    q0 = r'^\d:\s(.+):'
    q1 = r'inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    interface, ip = "", ""
    ifaces = {}
    for ln in outs:
        ln = ln.strip()
        m0 = re.search(q0, ln)
        if m0:
            interface = m0.group(1)
            ip = ""
            continue
        m = re.search(q1, ln)
        if m:
            ip = m.group(1)
        ifaces[interface] = ip
    return ifaces

def main():
    ''' main '''
    if not is_linux():
        prt('this script is for Linux only')
        sys.exit(1)
    ifaces = get_ipaddr()
    prt(ifaces)

if __name__ == "__main__":
    main()
