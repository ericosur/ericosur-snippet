#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position


'''
request sound list from pushover.net by using:
curl https://api.pushover.net/1/sounds.json?token=<apitoken>
'''

import argparse
import json
import os
import sys
import requests

# ruff: noqa: E402
sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from base_pushover import PushOverBase
from myutil import read_jsonfile


class Solution(PushOverBase):
    ''' PushOverBase will load the apitoken, userkey '''

    SOUNDS_CONFIG = 'pushover-sounds.json'
    URL = 'https://api.pushover.net/1/sounds.json?token='

    def __init__(self):
        super().__init__('')
        self.data = None
        self.debug = False
        self.use_local = True
        self.resp_str = ''

    def show_keys(self, jresp):
        ''' run '''
        sounds = jresp.get('sounds')
        print('show keys of sounds:')
        print(sounds.keys())

    def output_to_file(self, fn):
        ''' output to file '''
        with open(fn, "wt", encoding='UTF-8') as f:
            print(self.resp_str, file=f)
        print('output to:', fn)

    def read_localjson(self, fn):
        ''' read local json file '''
        if not os.path.exists(fn):
            print('[FAIL] local json file not found:', fn)
            return

        self.data = read_jsonfile(fn)
        for k,v in self.data.get('sounds').items():
            print(f'{k}: {v}')

    def shoot(self):
        ''' shoot '''
        if not self.apitoken or len(self.apitoken) <= 16:
            print('[WARN] api token not ok, exit...')
            return
        url = self.URL + self.apitoken
        if self.debug:
            print(url)
        r = requests.get(url, timeout=5.0)
        print(r.status_code)
        resp = r.json()
        self.resp_str = json.dumps(resp)
        if self.debug:
            self.show_resp()
        self.output_to_file(self.SOUNDS_CONFIG)
        self.show_keys(resp)

    @classmethod
    def run(cls, islocal, isdebug):
        ''' run '''
        obj = cls()
        if isdebug:
            obj.debug = isdebug
        if islocal:
            obj.read_localjson(cls.SOUNDS_CONFIG)
        else:
            obj.shoot()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description=__doc__)
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument('-l', '--local', action='store_true', default=True,
        help='(DEFAULT) will load sounds from:'+Solution.SOUNDS_CONFIG)
    parser.add_argument('-n', '--network', action='store_true',
        help='request sound list from remote')
    parser.add_argument("-d", "--debug", action='store_true', default=False,
        help='verbose mode')

    args = parser.parse_args()

    # to show help message directly
    #parser.print_help()

    if args.network:
        Solution.run(False, args.debug)
    else:
        print('[INFO] default using local file')
        Solution.run(args.local, args.debug)

if __name__ == '__main__':
    main()
