#!/usr/bin/env python3
# coding: utf-8

'''
reference: https://api.random.org/json-rpc/2/basic
'''

from __future__ import print_function
import json
import requests
import myutil

# pylint: disable=useless-object-inheritance
class RequestGuassian(object):
    ''' request guassian random numbers from random.org '''
    def __init__(self):
        self.sett_json = 'sett.json'
        self.data_file_name = ''
        self.resp_json = ''
        self.load_setting()
        self.apikey = self.get_apikey()

    def load_setting(self):
        ''' load setting '''
        if not myutil.isfile(self.sett_json):
            print('[FAIL] setting file not found: {}'.format(self.sett_json))
        sett = myutil.read_jsonfile(self.sett_json)
        self.data_file_name = sett.get('data_file_name')
        self.resp_json = sett.get('resp_json')

    def dump(self):
        ''' dump varialbes '''
        print('data_file_name: {}'.format(self.data_file_name))
        print('resp_json: {}'.format(self.resp_json))
        #print('apiKey: {}'.format(self.apiKey))

    @staticmethod
    def get_apikey():
        ''' get apikey '''
        import getapikey
        return getapikey.get_randomorg_apikey()

    def save_resp(self, resp):
        ''' save resp to json file '''
        with open(self.resp_json, 'w') as outj:
            outj.write(resp)

    def save_data(self, arr):
        ''' save array to data.txt '''
        mode = 'wt'
        if myutil.isfile('data.txt'):
            #print('file exists, use "at"')
            mode = 'at'
        with open(self.data_file_name, mode) as datafile:
            for elem in arr:
                print('{}'.format(elem), file=datafile)

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

        resp = requests.post(
            url, data=json.dumps(payload), headers=headers).json()

        print('save resp into file: {}'.format(self.resp_json))
        self.save_resp(json.dumps(resp))

        # responded id should the same as request
        #if resp['id'] == myid:
        #    print('id ok')

        # fetch a field not existed
        ret_data = resp.get('abc')
        if not ret_data is None:
            print('ret_data: {}'.format(ret_data))

        ret_data = []
        # get results
        if resp.get('result') is None:
            print('[FAIL] no result')
            errmsg = resp.get('error').get('message')
            print('[FAIL] error message: {}'.format(errmsg))
            return

        ret_data = resp.get('result').get('random').get('data')
        if ret_data is None:
            print('[FAIL] ret_data is None')
            return

        print('save to data file: {}'.format(self.data_file_name))
        self.save_data(ret_data)


def main():
    ''' main '''
    guas = RequestGuassian()
    guas.dump()
    guas.action()


if __name__ == "__main__":
    main()
