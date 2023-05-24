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
import requests

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile
from base_pushover import PushOverBase

class PushOverRequests(PushOverBase):
    ''' class to request pushover '''
    EXTRA_CONFIG = 'message.json'
    def __init__(self, msg):
        super().__init__(msg)
        self._title = 'p2over pushover'
        self.load_config(self.EXTRA_CONFIG)

    def load_config(self, fn):
        ''' load config '''
        data = read_jsonfile(fn)
        if data is None:
            print('[INFO] no extra data:', self.EXTRA_CONFIG)
            return
        self.message += data.get('sample')

    def is_keyready(self):
        ''' is apikey and token is ready? '''
        return self.userkey is None or self.apitoken is None

    def shoot(self):
        ''' shoot notification '''
        url = "https://api.pushover.net/1/messages.json"
        headers = {'content-type': 'application/json'}
        payload = {
            "token": self.apitoken,
            "user": self.userkey,
            "title": self.title,
            "message": self.message,
            "device": self.device,
            "sound": "intermission"
        }
        '''
        img_fn = self.get_home() + '/Pictures/kabaa.jpg'
        img = {
            "attachment": ("image.jpg", open(img_fn, "rb"), "image/jpeg")
        }
        '''
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5.0)
        print(r.status_code)
        resp = r.json()
        self.resp_str = json.dumps(resp)
        self.show_resp()


    @classmethod
    def run(cls, msg, device):
        '''
        pushover.net messages api reference:
        https://pushover.net/api#messages
        https://pushover.net/faq#library-python
        '''
        obj = cls(msg)
        if obj.is_keyready():
            print('[FAIL] key/apitoken not ready, exit...')
            sys.exit(1)
        obj.device = device
        obj.shoot()

def main():
    ''' main '''
    msg = ''' p2over.py
sends pushover notification
'''
    PushOverRequests.run(msg, device='erixiii')

if __name__ == '__main__':
    main()
