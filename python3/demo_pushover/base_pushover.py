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
import sys
from datetime import datetime
from time import time

sys.path.insert(0, "..")
from myutil import read_jsonfile, MyDebug, DefaultConfig


class PushOverBase(MyDebug):
    ''' base class of pushover '''
    def __init__(self, msg=""):
        super().__init__(False)
        # load user, token
        self.userkey = None
        self.apitoken = None
        self._device = None

        # load settings of previous three variables
        self.get_apikey()

        # default data fields
        self._title = 'pushover.py'
        self._message = f'{msg} at {datetime.now()}'
        self.resp_str = None

    def __str__(self):
        s = f'userkey: {self.userkey}\napitoken: {self.apitoken}\n'
        s += f'title: {self.title}\nmessage: {self.message}\ndevice: {self.device}\n'
        return s

    def is_keyready(self):
        ''' userkey and apitoken is ready? '''
        if self.debug:
            print(f'{self.userkey=}')
            print(f'{self.apitoken=}')
        return self.userkey and self.apitoken

    @abc.abstractmethod
    def shoot(self):
        ''' shoot, the inherited class MUST implement this function '''
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

    def get_apikey(self):
        ''' get apikey '''
        FN = 'pushover-net.json'
        config = DefaultConfig(FN).get_default_config()
        if not config:
            raise FileNotFoundError

        data = read_jsonfile(config)
        if data is None:
            raise ValueError("data is None")

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
