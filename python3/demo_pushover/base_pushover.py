#!/usr/bin/env python3


'''
pushover base class
'''

import os
from datetime import datetime
from time import time
import myutil

class PushOverBase(object):
    def __init__(self, msg):
        # load user, token
        (self.userkey, self.apitoken) = self.get_apikey()
        # default data fields
        self.title = 'pushover.py'
        self.message = '{} at {}'.format(msg, datetime.now())
        self.resp_str = None

    def __str__(self):
        return 'userkey: {}\napitoken: {}'.format(self.userkey, self.apitoken)

    def shoot(self):
        print('shoot!')

    def set_title(self, title):
        self.title = title

    def set_message(self, message):
        self.message = message

    def get_timestamp(self):
        return int(time())

    def show_resp(self):
        if not self.resp_str is None:
            print(self.resp_str)

    @staticmethod
    def get_home():
        home = os.environ.get('HOME')
        return home

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
    bar = PushOverBase('hello world')
    print(bar)
    bar.shoot()

if __name__ == '__main__':
    main()
