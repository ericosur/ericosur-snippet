#!/usr/bin/env python

'''
use module request to fetch specified web page
'''

# pip install requests
import requests


def main():
    '''main functon'''
    r = requests.get('https://tw.rter.info/capi.php', timeout=5)
    currency = r.json()
    print(currency)

if __name__ == '__main__':
    main()
