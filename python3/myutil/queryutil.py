#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions to query data from URL
'''

import json
import urllib.request

def query_url_for_data(url, debug=False):
    ''' query url and return data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = None
    if debug:
        print(url)

    with urllib.request.urlopen(url) as f:
        result = f.read()
    return result


def query_url_for_json(url):
    ''' query url and return json data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = query_url_for_data(url)
    data = json.loads(result)
    return data
