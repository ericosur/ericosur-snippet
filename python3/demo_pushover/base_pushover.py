#!/usr/bin/env python3
# coding: utf-8

'''
pushover base class
'''

from __future__ import print_function
import abc
import os
from datetime import datetime
from time import time
import myutil

class PushOverBase():
    ''' base class of pushover '''
    def __init__(self, msg):
        # load user, token
        self.userkey = None
        self.apitoken = None
        self._device = None
        # load settings of previous three variables
        if not self.get_apikey():
            print('[FAIL] failed to load config')
        # default data fields
        self._title = 'pushover.py'
        self._message = f'{msg} at {datetime.now()}'
        self.resp_str = None

    def __str__(self):
        s = f'userkey: {self.userkey}\napitoken: {self.apitoken}\n'
        s += f'title: {self.title}\nmessage: {self.message}\ndevice: {self.device}\n'
        return s

    @abc.abstractmethod
    def shoot(self):
        ''' shoot '''
        return NotImplemented

    @property
    def title(self):
        ''' title of notification '''
        return self._title

    @property
    def message(self):
        ''' message of notification '''
        return self._message

    @property
    def device(self):
        ''' device name of notification '''
        return self._device

    @staticmethod
    def get_timestamp():
        ''' get timestamp '''
        return int(time())

    def show_resp(self):
        ''' print resp '''
        if not self.resp_str is None:
            print(self.resp_str)

    @staticmethod
    def get_home():
        ''' $HOME '''
        home = os.environ.get('HOME')
        return home

    def get_apikey(self):
        ''' get apikey '''
        keyfile = 'pushover-net.json'
        home = os.environ.get('HOME')
        keypath = home + '/Private/' + keyfile
        if not myutil.isfile(keypath):
            print(f'[FAIL] key file not exist: {keypath}')
            return False
        data = myutil.read_jsonfile(keypath)
        if data is None:
            return False

        self.userkey = data.get('userkey')
        self.apitoken = data.get('apitoken')
        self._device = data.get('device')
        return True


def main():
    ''' main '''
    hello_world = PushOverBase('hello world')
    print(hello_world)
    hello_world.shoot()

if __name__ == '__main__':
    main()
