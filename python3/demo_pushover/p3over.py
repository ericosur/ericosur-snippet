#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#

'''
pushover.net is a web service to send notification to specified device

class PushOverRequests inherits from class PushOverBase for common functions
use module ==urllib== and ==http.client==
'''

import http.client
import urllib
from datetime import datetime
from base_pushover import PushOverBase


MODULE_NAME = "p3over.py"

class PushOverUrllib(PushOverBase):
    ''' pushover via urllib '''
    def __init__(self, msg=MODULE_NAME, title=MODULE_NAME):
        super().__init__(msg)
        self._sound = "incoming"
        self.title = title

    @property
    def sound(self) -> str:
        ''' sound of notification '''
        return self._sound
    @sound.setter
    def title(self, val: str):
        ''' setter of sound '''
        self._sound = val

    def shoot(self):
        '''
        pushover.net messages api reference:
        https://pushover.net/api#messages
        '''
        if not self.is_keyready():
            print('[FAIL] key/apitoken not ready, abort...')
            return

        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": self.apitoken,
                         "user": self.userkey,
                         "title": self.title,
                         "message": self.message,
                         "sound": self.sound
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        resp = conn.getresponse()
        self.resp_str = f'status: {resp.status} reason: {resp.reason}'
        self.show_resp()

    @classmethod
    def run(cls):
        ''' run '''
        ts = datetime.today().strftime('%a %d %b %Y, %H:%M') # Wed 24 May 2023, 14:49
        # strftime('%Y-%m-%d %H:%M:%S')  '2023-05-24 14:50:25'
        msg = f'notification on {ts} via urllib'

        obj = cls(msg=msg, title='demo by p3over.py')
        obj.shoot()

def main():
    ''' main '''
    PushOverUrllib.run()


if __name__ == '__main__':
    main()
