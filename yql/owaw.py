#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json
import os
from myutil import query_url_for_json, write_json

global latitude
global longitude

openweather_file = '/tmp/ow.json'
accuweather_file = '/tmp/aw_curr.json'
accuweather_forcast_file = '/tmp/aw_fore.json'

def getapikey(keyname):
    debug = False
    keyfn = os.environ["HOME"] + '/apikey/' + 'keys.json';
    with open(keyfn) as keyfile:
        data = json.load(keyfile)
    if debug:
        print(json.dumps(data))
    return data["keys"][keyname]["key"]

def my_write_json(filename, jsondata):
    write_json(filename, jsondata)
    print('query_openweather: output to {0}'.format(filename))


def query_openweather():
    debug = False
    appid = getapikey('openweather')
    baseurl = '''
    http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}
    '''.format(latitude, longitude, appid)
    baseurl = baseurl.strip()
    if debug:
        print(baseurl)
    data = query_url_for_json(baseurl)
    my_write_json(openweather_file, data)
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
    data = query_url_for_json(url)
    #print json.dumps(data)
    #write_json('aw.json', data)
    lockey = data["Key"]
    baseurl = '''
    http://dataservice.accuweather.com/currentconditions/v1/{0}?
    '''.format(lockey)
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({'apikey':appid})
    #print(url)
    data = query_url_for_json(url)
    my_write_json(accuweather_file, data)
    print('.[0].Temperature.Metric.Value: {0}'.format(data[0]['Temperature']['Metric']['Value']))

    baseurl = '''
    http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{0}?
    '''.format(lockey)
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({'apikey':appid, 'details':'true'})
    data = query_url_for_json(url)
    my_write_json(accuweather_forcast_file, data)
    print('.[0].RainProbability: {0}'.format(data[0]['RainProbability']))


if __name__ == '__main__':
    latitude = '25.292266'
    longitude = '121.567980'
    query_openweather()
    query_accuweather()
