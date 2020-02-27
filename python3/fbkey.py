#!/usr/bin/env python3
# coding: utf-8
#

''' compose fbkey string

    use 'adb shell getprop ro.boot.remainrebootcount'
    to get how many reboot remaining to lock
'''

#import os
import sys
import re
import subprocess

DEBUG = False
CLIPBOARD_AVAILABLE = False
try:
    import clipboard
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print('module clipboard not available...')

def exec_and_extract_hex(cmd):
    ''' test '''
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    pout = proc.communicate()
    if not pout:
        print('[ERROR] exec failed...')
        sys.exit(1)
    out = pout[0].decode("utf-8").strip()
    if DEBUG:
        print("program output:", out)
    reg = re.compile(r'([0-9A-Fa-f]{5,})', flags=re.M)
    m = reg.search(out)
    if m:
        if DEBUG:
            print(m.group(0))
        return m.group(0)

    #print('no match from:\n', out)
    return None

def try_adb(device_id):
    ''' try to use adb to get fbkey '''
    print('[INFO] using adb to collect...')
    remain = exec_and_extract_hex('adb shell getprop ro.boot.remainrebootcount')
    print('[INFO] current remain: {}'.format(remain))
    cpuid = exec_and_extract_hex('adb shell getprop ro.boot.msmserialno')
    msg = 'fbkey {} {} 100'.format(device_id, cpuid)
    return msg

def try_fastboot():
    ''' using fastboot '''
    device_id = exec_and_extract_hex("fastboot devices")
    print('device_id:', device_id)
    if not device_id:
        print('[ERROR] fastboot devices not found, exit...')
        sys.exit(1)
    cpuid = exec_and_extract_hex('fastboot getvar msmserialno 2>&1')
    print('cpuid:', cpuid)
    msg = 'fbkey {} {} 100'.format(device_id, cpuid)
    return msg


def main():
    ''' main '''
    adb_device_id = exec_and_extract_hex("adb devices")
    print('adb_device_id:', adb_device_id)
    msg = None
    if adb_device_id:
        msg = try_adb(adb_device_id)
    else:
        print('[ERROR] adb devices not found, try fastboot next...')
        msg = try_fastboot()

    print('msg:', msg)
    if msg and CLIPBOARD_AVAILABLE:
        print('[INFO] result is also stored into clipboard')
        clipboard.copy(msg)

if __name__ == '__main__':
    main()
