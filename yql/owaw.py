#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json
import os
from myutil import query_url, write_json

global latitude
global longitude

def getapikey(keyname):
    debug = False
    keyfn = os.environ["HOME"] + '/' + 'keys.json';
    with open(keyfn) as keyfile:
        data = json.load(keyfile)
    if debug:
        print(json.dumps(data))
    return data["keys"][keyname]["key"]

def query_openweather():
    debug = False
    appid = getapikey('openweather')
    baseurl = '''
    http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}
    '''.format(latitude, longitude, appid)
    baseurl = baseurl.strip()
    if debug:
        print(baseurl)
    data = query_url(baseurl)
    write_json('ow.json', data)
    tempk = data['main']['temp']
    tempk = tempk - 273.15
    print('temp:{0}'.format(tempk))
    print data['weather'][0]['description']



def query_accuweather():
    debug = False
    appid = getapikey('accuweather')
    baseurl = '''
    http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?
    '''
    pos = "{0},{1}".format(latitude, longitude)
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({'apikey':appid,'q':pos})
    if debug:
        print(url)
    data = query_url(url)
    #print json.dumps(data)
    #write_json('aw.json', data)
    lockey = data["Key"]
    baseurl = '''
    http://dataservice.accuweather.com/currentconditions/v1/{0}?
    '''.format(lockey)
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({'apikey':appid})
    #print(url)
    data = query_url(url)
    write_json('aw_curr.json', data)
    print data[0]['Temperature']['Metric']['Value']

    baseurl = '''
    http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{0}?
    '''.format(lockey)
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({'apikey':appid, 'details':'true'})
    data = query_url(url)
    write_json('aw_fore.json', data)


if __name__ == '__main__':
    latitude = '25.292266'
    longitude = '121.567980'
    query_openweather()
    query_accuweather()
