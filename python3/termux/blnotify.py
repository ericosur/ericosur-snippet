#!/usr/bin/env python
#coding: utf-8

'''
using termux-api
get battery level of device, issue notification if:
  - plug and battery level >= 79
  - unplug and battery level <= 40
'''

TEST = False

import os
import sys
import re
import json

def read_jsonfile(fn:str):
    '''
    specify json filename and return whole json object
    '''
    if not os.path.exists(fn):
        print(f'[FAIL] json file not found: {fn}')
        return None
    # read from json file
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)
    return data

def send_notification(msg: str):
    ''' send notification to phone via pushover.net service
    # use curl to send the notification request
    '''
    c = read_jsonfile("pushover.json")
    appkey = c.get("appkey")
    userkey = c.get("userkey")
    HOSTNAME = "pixel6a"
    preferdev = c.get("preferdev")
    cmd = f'''
    curl -s \\
        -F "token={appkey}"  \\
        -F "user={userkey}"  \\
        -F "title=From {HOSTNAME}"  \\
        -F "device={preferdev}"  \\
        -F "message={msg}"  \\
        https://api.pushover.net/1/messages.json
    '''
    if TEST:
        print(cmd)
    r = os.system(cmd)
    if r != 0:
        print('[FAIL] exit status:', r)
    print()

class Solution():
    ''' solution '''
    config = "termux-config.json"
    bjson = "bs.json"

    def __init__(self):
        self.percentage = None
        self.pluged = None

    def get_battery_status(self):
        ''' get battery status '''
        if not TEST:
            cmd = f'termux-battery-status > {Solution.bjson}'
            r = os.system(cmd)
            if r != 0:
                print('[FAIL] exit status:', r)
                sys.exit(-1)
        if not os.path.exists(Solution.bjson):
            print('[FAIL] result not found')
            sys.exit(-1)
        d = read_jsonfile(Solution.bjson)
        self.percentage = int(d.get('percentage'))
        self.plugged = d['plugged']
        print(f'{self.percentage=}, {self.plugged=}')

    def action(self):
        ''' action '''
        print('action')
        lower = 50
        upper = 80
        self.get_battery_status()
        msg = ''
        if not self.plugged and self.percentage < lower:
            msg = f'battery level {self.percentage} < {lower}, plz plug and charge...'
            send_notification(msg)
            return
        if self.plugged and self.percentage >= upper:
            msg = f'battery level = {self.percentage}, and almost charged, plz unplug...'
            send_notification(msg)
            return

        msg = f"battery level = {self.percentage}"
        send_notification(msg)

    @classmethod
    def run(cls):
        ''' runme '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
