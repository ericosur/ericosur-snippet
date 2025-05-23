#!python
# -*- coding: utf-8 -*-

r'''
call wmic and parse the output
try to find the pid of cmder/conemu, use wmic to get more info from
starting conemu64.exe like:

/Icon "D:\Tool\cmder\icons\cmder.ico" /title "Cmder"

note:
- prefix with raw because the backslash in this string
- 2025/4/09 modified for OA/windows
- it has a duplicated version in another repository
'''

import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from sysconfig import get_platform
try:
    #from rich import print as pprint
    from rich.pretty import pprint
    from rich.console import Console
    prt = pprint
    console = Console()
    logd = console.log
except ImportError:
    prt = print
    logd = print

def is_cygwin() -> bool:
    ''' is cygwin
        also "$OSTYPE" == *"cygwin"*
    '''
    p = get_platform()
    logd(p)
    return "cygwin" in p

def is_win() -> bool:
    ''' check if cygwin '''
    p = get_platform()
    logd(p)
    return "win" in p

def run_command2(cmd: str):
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

def run_in_termux() -> bool:
    ''' get prefix '''
    p = os.environ.get('PREFIX')
    if p is None:
        return False
    p = p.decode('utf-8')
    return "com.termux" in p

def get_tail_digits(s: str):
    ''' grep digits, return None or {k, v} '''
    #logd(s)
    n = s.strip().replace('\\','/').replace('"', ' ')
    #logd(f'{n=}')
    r1 = r'(Cmder)\s+(\d+)'
    r2 = r'(ConEmu64)\.exe\s+(\d+)'
    m1 = re.search(r1, n)
    if m1:
        k, v = m1.group(1), m1.group(2)
        return {k: v}
    m2 = re.search(r2, n)
    if m2:
        k, v = m2.group(1), m2.group(2)
        return {k: v}
    return None


class Solution:
    ''' call wmic and output to ahk config file
        if not found, will fill with a non-exist pid
    '''
    json_file = "cmder.json"
    AHK_FILE = "cmder.ahk"
    ahk_dir = "D:/Tool/AutoHotkey_2.0.17"
    default_pid = 32767

    def __init__(self):
        self.pwd = os.getcwd()
        self.module = sys.argv[0]
        logd(f'current dir: {self.pwd}')
        self.rets = {"Cmder": self.default_pid, "ConEmu64": self.default_pid}
        self.ahk_file = os.path.join(tempfile.gettempdir(), self.AHK_FILE)

    def run_wmic(self) -> None:
        ''' run wmic in cygwin/windows '''
        outs = run_command2('wmic process where "name=\'ConEmu64.exe\'" get ProcessId,CommandLine')
        if outs is None:
            return
        for i in outs:
            if len(i) > 0:
                r = get_tail_digits(i)
                if r:
                    self.rets.update(r)

    def get_timestr(self):
        ''' adjust local time with my own offset '''
        #utc_time = datetime.utcnow()
        utc_time = datetime.datetime.now(datetime.timezone.utc)
        # why time.timezone not work?
        # manually add 8 hours
        local_time_offset = datetime.timedelta(seconds=8*3600)
        #logd(utc_time)
        logd(f'manually offset: {local_time_offset}')
        local_time = utc_time + local_time_offset
        #logd(local_time)
        return local_time.strftime('%Y-%m-%d %H:%M:%S')

    def output_ahk(self) -> None:
        ''' output ahk file, will assign a default value if
            not found
        '''
        assert self.rets  # not possible

        fn = self.ahk_file
        with open(fn, "wt", encoding="UTF-8") as f:
            print(f'; ahk is generated by {self.module}', file=f)
            # also put timestamp into ahk file
            msg = self.get_timestr()
            logd(msg)
            print(f'; {msg}', file=f)
            print(f'; if pid is {self.default_pid}, it means cmder/conemu not found', file=f)
            v = self.rets.get("Cmder")
            print(f'cmder_pid := "{v}"', file=f)
            v = self.rets.get("ConEmu64")
            print(f'conemu_pid := "{v}"', file=f)
            epoch = int(time.time())
            print(f'wmic_epoch := {epoch}', file=f)
            logd(f'output to {fn}')

    def copy_ahk_to_dir(self):
        ''' copy ahk file to ahk dir, overwrite if exists '''
        if not os.path.exists(self.ahk_dir):
            logd(f"dir not found: {self.ahk_dir}")
            return
        # copy file to dst_dir
        try:
            shutil.copy(self.ahk_file, self.ahk_dir)
            logd(f'copy {self.ahk_file} to {self.ahk_dir}')
        except shutil.SameFileError:
            logd('same file, skip...')

    @classmethod
    def run(cls) -> None:
        ''' run '''
        obj = cls()
        obj.run_wmic()
        obj.output_ahk()
        obj.copy_ahk_to_dir()
        prt("NOTE: you need to reload Key3x3V2.ahk")


def main():
    ''' main '''
    if not is_win():
        prt("Not under windows")
        return
    Solution.run()

if __name__ == "__main__":
    main()
