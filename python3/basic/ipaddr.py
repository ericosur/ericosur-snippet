#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call __ip addr__ and parse
'''

import os
import re
import os
import sys

try:
    #from rich import print as pprint
    from rich.pretty import pprint
    prt = pprint
except ImportError:
    prt = print

from read_os_release import is_ubuntu1804
sys.path.insert(0, './')
sys.path.insert(0, '../')
sys.path.insert(0, 'python3/')
from myutil import is_linux, run_command  # type: ignore[import]

def run_in_termux() -> bool:
    ''' get prefix '''
    p = os.environ.get('PREFIX')
    if p is None:
        return False
    if isinstance(p, str):
        return "com.termux" in p
    return False

def get_ipaddr() -> dict[str, str]:
    ''' get ip addr'''
    cmd = "/sbin/ip addr" if is_ubuntu1804() else "/usr/sbin/ip addr"
    outs = run_command(cmd)
    if outs is None:
        return {}
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
    if run_in_termux():
        prt('no permission to call ip in termux')
        sys.exit(1)
    ifaces = get_ipaddr()
    prt(ifaces)

if __name__ == "__main__":
    main()
