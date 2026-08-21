#!/usr/bin/env python3

'''
call ifconfig and parse the output
'''

import argparse
import os
import re
import sys

try:
    from basic_common import get_prt, import_rich, logd, prt
    from read_os_release import is_ubuntu1804

    from myutil import (  # type: ignore[import]
        is_linux,
        is_windows,
        run_command,
        run_command2,
        show_platform,
    )
except ImportError as e:
    print('fail to import module: ', e)
    sys.exit(1)



def run_in_termux() -> bool:
    ''' get prefix '''
    p = os.environ.get('PREFIX')
    if p is None:
        return False
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
    from rich.table import Table
    table = Table(title="IP Address")
    table.add_column("interface", justify="left", style="cyan")
    table.add_column("inet", justify="left", style="magenta")
    table.add_column("MAC", justify="left", style="green")
    for d in ret:
        ifn = d.get('interface', '')
        inet = d.get('inet', '')
        mac = d.get('MAC', '')
        table.add_row(ifn, inet, mac)
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

    if is_linux():
        # note: if returns has no inet, it will be removed
        ret = get_ipaddr()
        if rich_available and not args.use_print and ret is not None:
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
