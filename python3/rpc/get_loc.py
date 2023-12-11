#!/usr/bin/env python3
# coding: utf-8

'''
https://github.com/ColdGrub1384/Pyto/issues/76
'''

import requests


def display_ip():
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json', timeout=5.0)
    my_ip = ip_request.json()['ip']
    req_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(req_url, timeout=5.0)
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})

if __name__ == '__main__':
    display_ip()
