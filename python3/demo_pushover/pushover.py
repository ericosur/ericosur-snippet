#!/usr/bin/env python3
# coding: utf-8

'''
pushover.net is a web service to send notification to specified device

it is fully self-contained function sample
'''

import argparse
from datetime import datetime
import http.client
import os
import platform
import time
import urllib
import myutil

def get_host():
    ''' get host name '''
    r = platform.node()
    if r is None or len(r) < 1:
        r = "kitty"
    return r

class Foobar():
    ''' basic class to send notification '''

    default_mobile_device = "erimx"

    def __init__(self, msg):
        (self.userkey, self.apitoken) = self.get_apikey()
        self.title = 'pushover.py'
        self.message = f'{get_host()}: {msg} at {datetime.now()}'

    def __str__(self):
        return 'userkey: {self.userkey}\napitoken: {self.apitoken}'

    def shoot(self):
        ''' shoot notification '''
        if self.userkey is None or self.apitoken is None:
            print('[FAIL] key/apitoken not exists, abort...')
            return

        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": self.apitoken,
                         "user": self.userkey,
                         "title": self.title,
                         "message": self.message,
                         "device": self.default_mobile_device
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        resp = conn.getresponse()
        print(f'status: {resp.status} reason: {resp.reason}')

    def set_title(self, title):
        ''' set title '''
        self.title = title

    def set_message(self, message):
        ''' set message '''
        self.message = message

    @staticmethod
    def get_timestamp():
        ''' get timestamp '''
        return int(time.time())

    @staticmethod
    def get_apikey():
        ''' get api key '''
        keyfile = 'pushover-net.json'
        userkey = None
        apitoken = None
        home = os.environ.get('HOME')
        keypath = home + '/Private/' + keyfile
        if not myutil.isfile(keypath):
            print(f'[FAIL] key file not exist: {keypath}')
            return None, None
        data = myutil.read_jsonfile(keypath)
        if data is None:
            return None, None

        userkey = data.get('userkey')
        apitoken = data.get('apitoken')
        return userkey, apitoken

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='python script to issue pushover notification')
    parser.add_argument("strings", metavar='str', type=str, nargs='*',
        help="issue notification with specific string")

    args = parser.parse_args()

    msg = ' '.join(args.strings)
    if len(msg) == 0:
        msg = 'test pushover notification!'
    print(msg)

    notif = Foobar(msg)
    notif.shoot()

if __name__ == '__main__':
    main()
