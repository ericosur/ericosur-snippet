#!/usr/bin/env python3
# coding: utf-8

'''
change the value of a json file which key field is "subject"
'''

# pylint: disable=invalid-name

import json
import os
import sys

# try to add my code snippet into python path
HOME = os.getenv('HOME')
p = os.path.join(HOME, '/src/ericosur-snippet/python3')
if os.path.exists(p):
    sys.path.insert(0, p)

try:
    import random_string
    import myutil
except ImportError:
    print('[ERROR] cannot import necessary module')
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
        self._prepare_possible_inputs()

    def _prepare_possible_inputs(self):
        ''' prepare possible inputs '''
        _fn = ChangeJson.TEST_JSON
        self.possible_inputs.append(_fn)
        _fn = os.path.join(HOME, ChangeJson.TEST_JSON)
        self.possible_inputs.append(_fn)
        _fn = os.path.join(HOME, 'Private', ChangeJson.TEST_JSON)
        self.possible_inputs.append(_fn)
        _fn = ChangeJson.TEMP_JSON
        self.possible_inputs.append(_fn)

    def load_data(self):
        ''' prepare '''
        for fn in self.possible_inputs:
            if os.path.exists(fn):
                print('load from:', fn)
                self.fn = fn
                self.data = myutil.read_jsonfile(self.fn)
                return
        print('[ERROR] data file not found, exit...')
        sys.exit(1)

    def modify_and_save(self):
        ''' modify content and save to file '''
        self.data['subject'] = self.request_random_string()
        with open(self.ofn, 'wt', encoding='utf8') as f:
            f.write(json.dumps(self.data, indent=4, sort_keys=False))
        print('[INFO] output to:', self.ofn)

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
