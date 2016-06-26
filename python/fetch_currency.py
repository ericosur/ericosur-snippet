#!/usr/bin/env python

# pip install requests

import requests

r=requests.get('https://tw.rter.info/capi.php')
currency=r.json()
print currency

