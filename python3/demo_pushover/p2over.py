#!/usr/bin/env python3
# coding: utf-8

'''
pushover.net is a web service to send notification to specified device

class PushOverRequests inherits from class PushOverBase for common functions
use module ==requests==
'''

import json
import requests
from base_pushover import PushOverBase

class PushOverRequests(PushOverBase):
    def __init__(self, msg):
        super().__init__(msg)
        self.title = 'push over requests'

    def shoot(self):
        '''
        pushover.net messages api reference:
        https://pushover.net/api#messages

        https://pushover.net/faq#library-python
        '''
        if self.userkey is None or self.apitoken is None:
            print('[FAIL] key/apitoken not exists, abort...')
            return

        url = "https://api.pushover.net/1/messages.json"
        headers = {'content-type': 'application/json'}
        payload = {
            "token": self.apitoken,
            "user": self.userkey,
            "title": self.title,
            "message": self.message,
            "sound": "intermission"
        }
        img_fn = self.get_home() + '/Pictures/kabaa.jpg'
        img = {
            "attachment": ("image.jpg", open(img_fn, "rb"), "image/jpeg")
        }

        r = requests.post(url, data=json.dumps(payload), headers=headers,
            files=img)
        print(r.status_code)

        resp = r.json()
        self.resp_str = json.dumps(resp)
        self.show_resp()


def main():
    gg = PushOverRequests('test pushover notification!')
    gg.shoot()

if __name__ == '__main__':
    main()
