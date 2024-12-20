#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call ip addr and parse
'''

import re
import subprocess
from rich import print as rprint
prt = rprint

def get_ipaddr() -> dict:
    ''' get ip addr'''
    cmd = "ip addr"
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) as p:
        p.wait()
        out = p.stdout.read().decode().split('\n')

    q0 = r'^\d:\s(.+):'
    q1 = r'inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    interface, ip = "", ""
    ifaces = {}
    for ln in out:
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
    ifaces = get_ipaddr()
    prt(ifaces)

if __name__ == "__main__":
    main()
