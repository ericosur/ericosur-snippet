#!/usr/bin/env python3
# coding: utf-8

'''
pushover.net is a web service to send notification to specified device

class PushOverRequests inherits from class PushOverBase for common functions
use module ==urllib== and ==http.client==
'''

import http.client, urllib
from base_pushover import PushOverBase

class PushOverUrllib(PushOverBase):
    def __init__(self, msg):
        super().__init__(msg)
        self.title = "push over urllib"

    def shoot(self):
        '''
        pushover.net messages api reference:
        https://pushover.net/api#messages
        '''
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
                "sound": "incoming"
            }), { "Content-type": "application/x-www-form-urlencoded" })
        resp = conn.getresponse()
        self.resp_str = 'status: {} reason: {}'.format(resp.status, resp.reason)
        self.show_resp()

def main():
    gg = PushOverUrllib('test pushover notification!')
    gg.shoot()

if __name__ == '__main__':
    main()
