#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
reference: https://api.random.org/json-rpc/2/basic
'''


import json
import sys

sys.path.insert(0, "..")
from myutil import read_jsonfile, isfile

try:
    import getapikey
    import requests
except ImportError as err:
    print('ImportError:', err)
    sys.exit(1)


class RequestGuassian():
    ''' request guassian random numbers from random.org '''
    DATAFILE = 'data.txt'
    def __init__(self):
        self.sett_json = 'sett.json'
        self.data_file_name = ''
        self.resp_json = ''
        self.load_setting()
        self.apikey = self.get_apikey()

    def load_setting(self):
        ''' load setting '''
        if not isfile(self.sett_json):
            print(f'[FAIL] setting file not found: {self.sett_json}')
        sett = read_jsonfile(self.sett_json)
        self.data_file_name = sett.get('data_file_name')
        self.resp_json = sett.get('resp_json')

    def show_brief(self):
        ''' dump varialbes '''
        print(f'data_file_name: {self.data_file_name}')
        print(f'resp_json: {self.resp_json}')
        #print(f'apiKey: {self.apiKey}')

    @staticmethod
    def get_apikey():
        ''' get apikey '''
        return getapikey.get_randomorg_apikey()

    def save_resp(self, resp):
        ''' save resp to json file '''
        with open(self.resp_json, 'wt', encoding='utf8') as outj:
            outj.write(resp)

    def save_data(self, arr):
        ''' save array to data file '''
        mode = 'wt'
        if isfile(self.DATAFILE):
            #print('file exists, use "at"')
            mode = 'at'
        with open(self.data_file_name, mode, encoding='utf8') as datafile:
            for elem in arr:
                print(f'{elem}', file=datafile)

    def action(self):
        '''
        perform request to random.org
        '''
        url = "https://api.random.org/json-rpc/2/invoke"
        headers = {'content-type': 'application/json'}

        myid = 47
        request_size = 1000

        if self.apikey == "":
            print('[FAIL] no api key, exit')
            return

        payload = {
            "jsonrpc": "2.0",
            "method": "generateGaussians",
            "params": {
                "apiKey": self.apikey,
                "n": request_size,
                "mean": 100,
                "standardDeviation": 15,
                "significantDigits": 6
            },
            "id": myid
        }

        resp = requests.post(url, data=json.dumps(payload),
                                headers=headers, timeout=5.0).json()

        print(f'save resp into file: {self.resp_json}')
        self.save_resp(json.dumps(resp))

        # responded id should the same as request
        #if resp['id'] == myid:
        #    print('id ok')

        # fetch a field not existed
        ret_data = resp.get('abc')
        if not ret_data is None:
            print(f'ret_data: {ret_data}')

        ret_data = []
        # get results
        if resp.get('result') is None:
            print('[FAIL] no result')
            errmsg = resp.get('error').get('message')
            print(f'[FAIL] error message: {errmsg}')
            return

        ret_data = resp.get('result').get('random').get('data')
        if ret_data is None:
            print('[FAIL] ret_data is None')
            return

        print(f'save to data file: {self.data_file_name}')
        self.save_data(ret_data)

    @classmethod
    def run(cls):
        ''' run '''
        obj = RequestGuassian()
        obj.show_brief()
        obj.action()

def main():
    ''' main '''
    RequestGuassian.run()


if __name__ == "__main__":
    main()
