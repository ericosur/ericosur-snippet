#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#

'''
pushover base class
'''

import abc
import os
from datetime import datetime
from time import time
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile

class PushOverBase():
    ''' base class of pushover '''
    def __init__(self, msg):
        # load user, token
        self.userkey = None
        self.apitoken = None
        self._device = None
        # load settings of previous three variables
        if not self.get_apikey():
            print('[FAIL] failed to load config, exit...')
            sys.exit(1)
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
    def title(self) -> str:
        ''' title of notification '''
        return self._title
    @title.setter
    def title(self, val: str):
        ''' setter of title '''
        self._title = val

    @property
    def message(self) -> str:
        ''' message of notification '''
        return self._message
    @message.setter
    def message(self, val: str):
        ''' setter of message '''
        self._message = val

    @property
    def device(self) -> str:
        ''' device name of notification '''
        return self._device
    @device.setter
    def device(self, val: str):
        ''' setter for device '''
        self._device = val

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
        home = os.environ.get('HOME')
        keypath = os.path.join(home, 'Private', 'pushover-net.json')
        if not os.path.exists(keypath):
            print(f'[FAIL] key file not exist: {keypath}')
            return False
        data = read_jsonfile(keypath)
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
