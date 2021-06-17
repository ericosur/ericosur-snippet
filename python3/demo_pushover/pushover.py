#!/usr/bin/env python3
# coding: utf-8

'''
pushover.net is a web service to send notification to specified device

it is fully self-contained function sample
'''

from __future__ import print_function
import os
from datetime import datetime
import sys
import time
import http.client
import urllib
import myutil

class FooBar():
    ''' basic class to send notification '''
    def __init__(self, msg):
        (self.userkey, self.apitoken) = self.get_apikey()
        self.title = 'pushover.py'
        self.message = '{} at {}'.format(msg, datetime.now())

    def __str__(self):
        return 'userkey: {}\napitoken: {}'.format(self.userkey, self.apitoken)

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
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        resp = conn.getresponse()
        print('status: {} reason: {}'.format(resp.status, resp.reason))

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
            print('[FAIL] key file not exist: {}'.format(keypath))
            return None, None
        data = myutil.read_jsonfile(keypath)
        if data is None:
            return None, None

        userkey = data.get('userkey')
        apitoken = data.get('apitoken')
        return userkey, apitoken

def main(msg):
    ''' main '''
    if msg:
        print(msg)
    else:
        msg = 'test pushover notification!'

    gg = FooBar(msg)
    gg.shoot()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main(None)
