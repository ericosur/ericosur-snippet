#!/usr/bin/env python
# -*- coding: utf-8 -*-

# use yql to query yahoo weather
# to get pretty output:
# ./yql.py|python -m json.tool
#
# from: http://57life.blogspot.tw/2012/12/msn-yahoo.html
# 20070568   台北 (台北市內湖區)

import sys
import urllib2, urllib, json

debug = False

def help_message():
    helpmsg='''
    insufficient arguments:
    -1 to query all woeid, or
    0-{0} to query woeid also query yahoo weather
    '''.format(len(loc))
    helpmsg = helpmsg.strip()
    print(helpmsg)
    print("you may use 'python -m json.tool' to get pretty format\n")


'''
/usr/bin/curl https://query.yahooapis.com/v1/public/yql \
    -d q='select * from geo.places where text="(-15.763,-47.870)"' \
    -d 'format=json'
'''

def query_woeid_by_latlong(latitude, longitude, condition='woeid', getAll=False):
    '''
    only query woeid by latitude/longitude
    '''
    tmp = '''
        select {0} from geo.places where text ="({1},{2})"
    '''.format(condition, latitude, longitude)
    yql_query = tmp.strip()
    data = issue_yql(yql_query)
    if condition == 'woeid':
        print json.dumps(data)

    if getAll:
        return json.dumps(data)
    else:
        return json.dumps(data['query']['results']['place']['woeid'])


def print_weather_result(data):
    print json.dumps(data['query']['results']['channel']['description'])
    print json.dumps(data['query']['results']['channel']['item']['condition'])


def issue_yql(yql_query):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    return data


def query_weather(woeid):
    '''
    query weather by assigning woeid
    '''
    condition = '*'
    tmp = '''
        select {0} from weather.forecast where woeid={1} and u=\'c\'
    '''.format(condition, woeid)
    yql_query = tmp.strip()
    print_weather_result( issue_yql(yql_query) )


def query_weather_loc(latitude, longitude):
    '''
    given latitude/longitude, query woeid in select sub statement and
    query weather
    '''
    condition = '*'
    tmp = '''
        select {0} from weather.forecast where woeid in (select woeid
        from geo.places where text="({1},{2})") and u=\'c\'
    '''.format(condition, latitude, longitude)
    yql_query = tmp.strip()
    print_weather_result( issue_yql(yql_query) )


# predefined latitude/longitude for some POI
loc = [
    [25.033827, 121.565768],  # Taipei 101
    [-15.763250, -47.870459], # Universidade de Brasília
    [37.421282, -122.086989], # googleplex, mountain view CA
    [40.689201, -74.044382],  # staue of liberty
    [51.500760, -0.124296],   # Ben clock at London
    [35.658519, 139.745529],  # tokyo tower
    [29.975278, 31.138007],   # great sphinx
    [1.286859, 103.854854],   # merlion
    [-43.529076, 172.623976], # north hagley park christchurch
    [21.361145, -157.948567], # pearl harbor
    [-33.908068, 18.418042],  # two oceans aquarium
    [30.328448, 35.444428],   # petra jordan
    [-2.228088, 38.559125],   # kitui
    [21.422399, 39.827339],   # kaaba
]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if (sys.argv[1] == '-h') or (sys.argv[1] == '-?'):
            help_message()
            sys.exit()

        if sys.argv[1] == '-1':
            print("query all...")
            for oneloc in loc:
                query_woeid_by_latlong(oneloc[0], oneloc[1])
        elif sys.argv[1] == '-a':
            #print("full woeid for #0")
            oneloc = loc[0]
            print( query_woeid_by_latlong(oneloc[0], oneloc[1], "*", True) )

        else:
            idx = int(sys.argv[1])
            if len(loc) >= idx:
                oneloc = loc[idx]
                wid = query_woeid_by_latlong(oneloc[0], oneloc[1], "*")
                query_weather(wid)
            else:
                print("unknown opt: {0}".format(sys.argv[1]))
    else:
        oneloc = loc[7]
        query_weather_loc(oneloc[0], oneloc[1])
