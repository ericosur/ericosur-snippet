#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#

'''
pushover.net is a web service to send notification to specified device

class PushOverRequests inherits from class PushOverBase for common functions
use module ==requests==
'''

import json
import sys
from random import choice
from time import time
import requests
from base_pushover import PushOverBase
sys.path.insert(0, "..")
from myutil import read_jsonfile

MODULE_NAME = 'p2over.py'

class PushOverRequests(PushOverBase):
    ''' class to request pushover '''

    # change the value of each field to send different notification
    EXTRA_CONFIG = 'settings-p2over.json'

    def __init__(self, msg=MODULE_NAME):
        super().__init__(msg)
        self.title = ''
        self.message = msg
        self.sound = ''
        self.device = ''
        self.config_ok = None
        self.load_config(self.EXTRA_CONFIG)

    def load_config(self, fn):
        ''' load config '''
        data = read_jsonfile(fn)
        if data is None:
            print('[INFO] no extra data:', self.EXTRA_CONFIG)
            self.config_ok = False
            raise ValueError
        self.config_ok = True
        self.title = f"{data.get('title')} {int(time())}"
        self.device = data.get('device')
        # load message from a list
        messages = data.get('messages')
        self.message = choice(messages)
        # set a default, and pick one from sounds
        sounds = list(data.get('sounds').keys())
        self.sound = choice(sounds)

    def shoot(self, DRY_RUN=False):
        ''' shoot notification '''
        if not self.is_keyready():
            print('[FAIL] key/apitoken not ready, exit...')
            sys.exit(1)

        url = "https://api.pushover.net/1/messages.json"
        headers = {'content-type': 'application/json'}
        payload = {
            "token": self.apitoken,
            "user": self.userkey,
            "title": self.title,
            "message": self.message,
            "device": self.device,
            "sound": self.sound
        }

        # img_fn = self.get_home() + '/Pictures/kabaa.jpg'
        # img = {
        #     "attachment": ("image.jpg", open(img_fn, "rb"), "image/jpeg")
        # }

        if DRY_RUN:
            print('[INFO] dry run only...')
            self.dump_payload(payload)
            return

        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5.0)
        self.show_result(r)

    def show_result(self, ret):
        ''' show result '''
        resp = ret.json()
        self.resp_str = json.dumps(resp)
        print(f'status: {ret.status_code}, resp: {self.resp_str}')

    @staticmethod
    def dump_payload(p):
        ''' dump payload '''
        fields = ['title', 'message', 'device', 'sound']
        for f in fields:
            print(f'{f}: {p.get(f)}')

    @classmethod
    def run(cls):
        '''
        pushover.net messages api reference:
        https://pushover.net/api#messages
        https://pushover.net/faq#library-python
        '''
        DRY_RUN = True
        obj = cls()
        obj.shoot(DRY_RUN)

def main():
    ''' main '''
    PushOverRequests.run()

if __name__ == '__main__':
    main()
