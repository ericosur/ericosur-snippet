#!/usr/bin/env python3
# coding: utf-8

'''
using pushover to send notification to my iphone
'''

import os
import sys
from datetime import datetime
import time
import http.client, urllib
import myutil

class foobar(object):
    def __init__(self, msg):
        (self.userkey, self.apitoken) = self.get_apikey()
        self.title = 'pushover.py'
        self.message = '{} at {}'.format(msg, datetime.now())

    def show(self):
        print('userkey: {}\napitoken: {}'.format(self.userkey, self.apitoken))

    def shoot(self):
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
            }), { "Content-type": "application/x-www-form-urlencoded" })
        resp = conn.getresponse()
        print('status: {} reason: {}'.format(resp.status, resp.reason))

    def set_title(self, title):
        self.title = title

    def set_message(self, message):
        self.message = message

    def get_timestamp(self):
        return int(time.time())

    @staticmethod
    def get_apikey():
        keyfile = 'pushover-net.json'
        userkey = None
        apitoken = None
        home = os.environ.get('HOME')
        keypath = home + '/Private/' + keyfile
        if not myutil.isfile(keypath):
            print('[FAIL] key file not exist: {}'.format(keypath))
            return None, None
        data = myutil.read_jsonfile(keypath)
        if data is None:
            return None, None

        userkey = data.get('userkey')
        apitoken = data.get('apitoken')
        return userkey, apitoken

def main():
    gg = foobar('test pushover notification!')
    gg.shoot()

if __name__ == '__main__':
    main()
