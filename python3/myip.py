#!/usr/bin/env python3
# coding: utf-8

'''
use api.myip.com to get current public ip
and use ip-api.com to get location of such ip
'''

import sys
import json
import requests

def get_current_ip():
    ''' use this to get myip '''
    url = 'https://api.myip.com'
    r = requests.get(url)
    print('url:', r.url)
    print('r.json:\n', r.json())
    data = r.json()
    ip = data['ip']
    return ip

def get_ip_info(ip):
    ''' use this to get IP location and related data '''
    iploc = f'http://ip-api.com/json/{ip}'
    r = requests.get(iploc)
    print('url:', r.url)
    print('r.json:\n', json.dumps(r.json()))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        get_ip_info(get_current_ip())
    else:
        get_ip_info(sys.argv[1])
