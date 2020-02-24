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

def exec_and_extract_hex(cmd):
    ''' test '''
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    pout = proc.communicate()
    if not pout:
        print('None')
        sys.exit(1)
    out = pout[0].decode("utf-8").strip()
    #print("program output:", out)
    reg = re.compile(r'(^[0-9A-Fa-f]+)', flags=re.M)
    m = reg.search(out)
    if m:
        #print(m.group(0))
        return m.group(0)

    print('no match from:\n', out)
    return None


def main():
    ''' main '''
    devid = exec_and_extract_hex("adb devices")
    if not devid:
        print('[ERROR] adb devices not found')
        sys.exit(1)

    print('[INFO] using adb to collect...')
    remain = exec_and_extract_hex('adb shell getprop ro.boot.remainrebootcount')
    print('[INFO] current remain: {}'.format(remain))
    cpuid = exec_and_extract_hex('adb shell getprop ro.boot.msmserialno')
    msg = 'fbkey {} {} 100'.format(devid, cpuid)
    print(msg)
    # pylint: disable=import-outside-toplevel
    try:
        import clipboard
        clipboard.copy(msg)
        print('[INFO] result is also stored into clipboard')
    except ImportError:
        pass

if __name__ == '__main__':
    main()
