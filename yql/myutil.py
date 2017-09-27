#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib2, json

def query_url(url):
    debug = False
    if debug:
        print(url)
    result = urllib2.urlopen(url).read()
    data = json.loads(result)
    return data

def write_json(fn, data):
    with open(fn, 'w') as ofile:
        ofile.write(json.dumps(data))
        print('output json to {0}'.format(fn))
