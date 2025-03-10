#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=invalid-name
#

'''
Change the value of a specified key "subject" in a json file.
The other keys/fields will not be changed.

try this:
    python3 change_subject.py 2>/dev/null && cat /tmp/__out__.json
'''

import json
import sys

from myutil import read_jsonfile, DefaultConfig

try:
    import random_string
except ImportError:
    print('[ERROR] cannot import random_string', file=sys.stderr)
    sys.exit(1)

class ChangeJson():
    ''' change json '''
    TEST_JSON = 'set-send-attach.json'
    TEMP_JSON = '/tmp/__out__.json'

    def __init__(self):
        self.fn = None
        self.ofn = ChangeJson.TEMP_JSON
        self.data = None
        self.possible_inputs = []

    def load_data(self):
        ''' prepare '''
        self.fn = DefaultConfig(self.TEST_JSON).get_default_config()
        if self.fn is None:
            raise FileNotFoundError(self.TEST_JSON)

        self.data = read_jsonfile(self.fn)
        if self.data is None:
            raise ValueError("data is None")

    def modify_and_save(self):
        ''' modify content and save to file '''
        self.data['subject'] = self.request_random_string()
        with open(self.ofn, 'wt', encoding='utf8') as f:
            f.write(json.dumps(self.data, indent=4, sort_keys=False))
            print(file=f)
        print(f'[INFO] output to: {self.ofn}', file=sys.stderr)

    @staticmethod
    def request_random_string():
        ''' request random string '''
        s = random_string.Solution()
        r = s.request_words(7)
        return r

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.load_data()
        obj.modify_and_save()

def main():
    ''' main '''
    ChangeJson.run()

if __name__ == '__main__':
    main()
