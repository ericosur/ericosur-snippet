#!/usr/bin/env python
# -*- coding: utf-8 -*-

# use google geocoding API to query location, address, and etc.
# refer to:
# https://github.com/google/open-location-code/wiki/Plus-codes-API
#

import sys, os
import urllib2, urllib, json

debug = False
apikey = ''
email = ''

def help_message():
    helpmsg='''
    insufficient arguments
    '''
    print(helpmsg.strip())

def read_secret():
    '''
    read apikey and email address from ~/apikey/apikey.json
    sample content:
    {
      "geocoding": {
        "apikey": "12345678"
      },
      "email": "user@sample.com"
    }
    '''
    global apikey
    global email
    home = os.environ.get('HOME')
    file = home + '/apikey/apikey.json'
    # read from json file
    with open(file) as sec_file:
        data = json.load(sec_file)
    apikey = data['geocoding']['apikey']
    email = data['email']
    if debug:
        print("apikey:{0}\nemail:{1}".format(apikey, email))


'''
URL="https://plus.codes/api?address=${ADDR}&ekey=${KEY}&${EMAIL}"
'''
def query_geocoding(addr, key, email):
    baseurl = "https://plus.codes/api?"
    yql_url = baseurl + urllib.urlencode({'address':addr,'ekey':key}) + "&" + email
    print yql_url
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    #print json.dumps(data)
    if data['status'] == 'OK':
        return data
    else:
        return None

def show_result(data):
    if data == None:
        return

    val = data['plus_code']['best_street_address']
    print("best_street_address:" + val)
    val = data['plus_code']['global_code']
    print("global_code:" + val)

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     if (sys.argv[1] == '-h') or (sys.argv[1] == '-?'):
    #         help_message()
    #         sys.exit()
    read_secret()
    ret = query_geocoding("自由女神像", apikey, email)
    show_result(ret)
