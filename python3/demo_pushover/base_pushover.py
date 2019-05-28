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
        self.userkey = None
        self.apitoken = None
        self.device = None
        # load settings of previous three variables
        if not self.get_apikey():
            print('[FAIL] failed to load config')
        # default data fields
        self.title = 'pushover.py'
        self.message = '{} at {}'.format(msg, datetime.now())
        self.resp_str = None

    def __str__(self):
        s = 'userkey: {}\napitoken: {}\n'.format(self.userkey, self.apitoken)
        s += 'title: {}\nmessage: {}\ndevice: {}\n'.format(
            self.title, self.message, self.device)
        return s

    def shoot(self):
        print('shoot!')

    def set_title(self, title):
        self.title = title

    def set_message(self, message):
        self.message = message

    def set_device(self, device):
        self.device = device

    def get_timestamp(self):
        return int(time())

    def show_resp(self):
        if not self.resp_str is None:
            print(self.resp_str)

    @staticmethod
    def get_home():
        home = os.environ.get('HOME')
        return home

    def get_apikey(self):
        keyfile = 'pushover-net.json'
        home = os.environ.get('HOME')
        keypath = home + '/Private/' + keyfile
        if not myutil.isfile(keypath):
            print('[FAIL] key file not exist: {}'.format(keypath))
            return False
        data = myutil.read_jsonfile(keypath)
        if data is None:
            return False

        self.userkey = data.get('userkey')
        self.apitoken = data.get('apitoken')
        self.device = data.get('device')
        return True


def main():
    bar = PushOverBase('hello world')
    print(bar)
    bar.shoot()

if __name__ == '__main__':
    main()
