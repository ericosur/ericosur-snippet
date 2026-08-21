#!/usr/bin/env python3

'''
call __ip addr__ and parse
'''

import argparse
import os
import re
import sys

from basic_common import get_prt, import_rich, prt

try:
    from read_os_release import is_ubuntu1804

    from myutil import is_linux, run_command  # type: ignore[import]
except ImportError as e:
    prt("failed to import module: ", e)
    sys.exit(1)

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

def show_as_table(ifaces: dict[str, str]) -> None:
    ''' show as table '''
    from rich.table import Table
    table = Table(title="IP Address")
    table.add_column("interface", justify="left", style="cyan")
    table.add_column("inet", justify="left", style="magenta")
    for interface, ip in ifaces.items():
        table.add_row(interface, ip)
    prt(table)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='Show network interface addresses')
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('-r', '--rich', action='store_true',
        help='explicitly use rich module; fail if rich is unavailable')
    output_group.add_argument('-p', '--print', action='store_true', dest='use_print',
        help='explicitly use stdlib print only')
    args = parser.parse_args()

    global prt  # pylint: disable=global-statement
    prt = get_prt(use_print=args.use_print)

    rich_available = import_rich()
    if args.rich and not rich_available:
        parser.error('rich module is required when using --rich/-r')

    if not is_linux():
        prt('this script is for Linux only')
        sys.exit(1)
    if run_in_termux():
        prt('no permission to call ip in termux')
        sys.exit(1)
    ifaces = get_ipaddr()
    if rich_available and not args.use_print:
        show_as_table(ifaces)
    else:
        prt(ifaces)

if __name__ == "__main__":
    main()
