#!/usr/bin/env python3
# coding: utf-8

'''
reference: https://api.random.org/json-rpc/2/basic
'''
from __future__ import print_function
import json
import random
import requests
from getapikey import get_randomorg_apikey

def main():
    ''' main '''
    url = "https://api.random.org/json-rpc/2/invoke"
    headers = {'content-type': 'application/json'}

    myid = random.randint(1, 100)
    key = get_randomorg_apikey()
    request_size = 10

    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": key,
            "n": request_size,
            "min": 1,
            "max": 6,
            "replacement": True
        },
        "id": myid
    }

    resp = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(json.dumps(resp))

    # responded id should the same as request
    if resp['id'] == myid:
        print('id matched')

    # fetch a field not existed
    ret_data = resp.get('abc')
    if not ret_data is None:
        print('ret_data: {}'.format(ret_data))

    # get results
    ret_data = resp.get('result').get('random').get('data')
    if not ret_data is None:
        print('ret_data: {}'.format(ret_data))


if __name__ == "__main__":
    main()
