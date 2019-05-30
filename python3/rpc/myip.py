#!/usr/bin/env python3
# coding: utf-8

import requests

# use this to get myip
url = 'https://api.myip.com'
r = requests.get(url)
print(r.url)
print(r.json())
data = r.json()
ip = data['ip']

# use this to get IP location and related data
iploc = 'http://ip-api.com/json/{}'.format(ip)
r = requests.get(iploc)
print(r.url)
print(r.json())
