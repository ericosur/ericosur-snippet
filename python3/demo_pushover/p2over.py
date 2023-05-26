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

import os
import json
import sys
from random import choice
from time import time
import requests

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile
from base_pushover import PushOverBase

class PushOverRequests(PushOverBase):
    ''' class to request pushover '''

    # change the value of each field to send different notification
    EXTRA_CONFIG = 'settings-p2over.json'

    def __init__(self, msg):
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
            return
        self.config_ok = True
        self.title = f"{data.get('title')} {int(time())}"
        self.device = data.get('device')
        # load message from a list
        messages = data.get('messages')
        self.message = choice(messages)
        # set a default, and pick one from sounds
        sounds = list(data.get('sounds').keys())
        self.sound = choice(sounds)

    def is_keyready(self):
        ''' is apikey and token is ready? '''
        return self.userkey is None or self.apitoken is None

    def shoot(self):
        ''' shoot notification '''
        if not self.config_ok:
            print('[WARN] need check config, exit...')
            return

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
        '''
        img_fn = self.get_home() + '/Pictures/kabaa.jpg'
        img = {
            "attachment": ("image.jpg", open(img_fn, "rb"), "image/jpeg")
        }
        '''
        self.dump_payload(payload)
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5.0)
        print(r.status_code)
        resp = r.json()
        self.resp_str = json.dumps(resp)
        self.show_resp()

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
        obj = cls("")
        if obj.is_keyready():
            print('[FAIL] key/apitoken not ready, exit...')
            sys.exit(1)
        obj.shoot()

def main():
    ''' main '''
    PushOverRequests.run()

if __name__ == '__main__':
    main()
