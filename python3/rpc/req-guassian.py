#!/usr/bin/env python3
# coding: utf-8

'''
reference: https://api.random.org/json-rpc/2/basic
'''

import requests
import json
import myutil

class Request_Guassian(object):
    def __init__(self):
        self.sett_json = 'sett.json'
        self.data_file_name = ''
        self.resp_json = ''
        self.apiKey = ''
        self.load_setting()
        self.apiKey = self.get_apikey()

    def load_setting(self):
        if not myutil.isfile(self.sett_json):
            print('[FAIL] setting file not found: {}'.format(self.sett_json))
        sett = myutil.read_jsonfile(self.sett_json)
        self.data_file_name = sett.get('data_file_name')
        self.resp_json = sett.get('resp_json')

    def dump(self):
        print('data_file_name: {}'.format(self.data_file_name))
        print('resp_json: {}'.format(self.resp_json))
        #print('apiKey: {}'.format(self.apiKey))

    def get_apikey(self):
        import getapikey
        return getapikey.get_randomorg_apikey()

    def save_resp(self, resp):
        with open(self.resp_json, 'w') as outj:
            outj.write(resp)

    def save_data(self, arr):
        mode = 'wt'
        if myutil.isfile('data.txt'):
            #print('file exists, use "at"')
            mode = 'at'
        with open(self.data_file_name, mode) as datafile:
            for elem in arr:
                print('{}'.format(elem), file=datafile)

    def action(self):
        url = "https://api.random.org/json-rpc/2/invoke"
        headers = {'content-type': 'application/json'}

        myid = 47
        request_size = 1000

        payload = {
            "jsonrpc": "2.0",
            "method": "generateGaussians",
            "params": {
                "apiKey": self.apiKey,
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

        # get results
        ret_data = resp.get('result').get('random').get('data')
        if ret_data is None:
            print('[FAIL] data is None')
            return

        print('save to data file: {}'.format(self.data_file_name))
        self.save_data(ret_data)


def main():
    foo = Request_Guassian()
    foo.dump()
    foo.action()


if __name__ == "__main__":
    main()
