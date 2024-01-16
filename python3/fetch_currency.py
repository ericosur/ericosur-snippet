#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
use module request to fetch specified web page
'''

from __future__ import print_function
# pip install requests
import requests

def main():
    '''main functon'''
    r = requests.get('https://tw.rter.info/capi.php', timeout=5)
    currency = r.json()
    print(currency)

if __name__ == '__main__':
    main()
