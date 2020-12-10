#!/usr/bin/python3.6
# coding: utf-8

'''
change the value of a json file which key field is "subject"
'''

# pylint: disable=invalid-name

import json
import os
import sys

HOME = os.getenv('HOME')
sys.path.insert(0, HOME + '/src/ericosur-snippet/python3')
try:
    import random_string
    import myutil
except ImportError:
    print('[ERROR] cannot import necessary module')
    sys.exit(1)

class ChangeJson():
    ''' change json '''
    def __init__(self):
        self.fn = HOME + '/set-send-attach.json'
        self.ofn = '/tmp/out.json'
        self.data = None

    def prepare(self):
        ''' prepare '''
        self.data = myutil.read_jsonfile(self.fn)

    @staticmethod
    def request_random_string():
        ''' request random string '''
        s = random_string.Solution()
        r = s.request_words(7)
        return r

    def action(self):
        ''' action '''
        self.prepare()
        self.data['subject'] = self.request_random_string()
        with open(self.ofn, 'wt') as f:
            f.write(json.dumps(self.data, indent=4, sort_keys=False))


def main():
    ''' main '''
    cj = ChangeJson()
    cj.action()

if __name__ == '__main__':
    main()
